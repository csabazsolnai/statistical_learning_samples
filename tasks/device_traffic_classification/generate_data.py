"""
Generates a synthetic home-network device-traffic dataset for practice (see
TASK.md in this folder). Not a real dataset or task from any company --
built to be plausible for a network-intelligence device classification
problem: per-device aggregated traffic stats with a
device_type label, imbalanced classes, some missing values, and a couple of
injected outliers, so the practice run forces the same data-quality and
class-imbalance decisions a real task likely would.

Run this once to produce traffic_data.csv, then work the task in TASK.md
without re-reading this file (it would spoil the EDA).
"""

import numpy as np
import pandas as pd

rng = np.random.default_rng(42)

DEVICE_PROFILES = {
    "laptop": dict(n=220, bytes_mu=4.2e8, bytes_sigma=1.5e8, pkts_mu=350000, pkts_sigma=90000,
                   conns_mu=180, conns_sigma=40, dur_mu=45, dur_sigma=20, ports_mu=60, ports_sigma=20,
                   ips_mu=90, ips_sigma=30, tcp_ratio_mu=0.85, night_ratio_mu=0.15),
    "smart_tv": dict(n=160, bytes_mu=9.0e8, bytes_sigma=2.0e8, pkts_mu=600000, pkts_sigma=120000,
                      conns_mu=40, conns_sigma=10, dur_mu=900, dur_sigma=300, ports_mu=8, ports_sigma=3,
                      ips_mu=15, ips_sigma=5, tcp_ratio_mu=0.70, night_ratio_mu=0.25),
    "ip_camera": dict(n=90, bytes_mu=2.0e8, bytes_sigma=5.0e7, pkts_mu=400000, pkts_sigma=80000,
                        conns_mu=20, conns_sigma=5, dur_mu=1800, dur_sigma=400, ports_mu=3, ports_sigma=1,
                        ips_mu=4, ips_sigma=2, tcp_ratio_mu=0.95, night_ratio_mu=0.45),
    "smart_speaker": dict(n=70, bytes_mu=3.0e7, bytes_sigma=1.0e7, pkts_mu=25000, pkts_sigma=8000,
                            conns_mu=60, conns_sigma=15, dur_mu=12, dur_sigma=5, ports_mu=5, ports_sigma=2,
                            ips_mu=8, ips_sigma=3, tcp_ratio_mu=0.90, night_ratio_mu=0.10),
    "smart_thermostat": dict(n=35, bytes_mu=5.0e6, bytes_sigma=2.0e6, pkts_mu=4000, pkts_sigma=1500,
                               conns_mu=30, conns_sigma=8, dur_mu=5, dur_sigma=2, ports_mu=2, ports_sigma=1,
                               ips_mu=3, ips_sigma=1, tcp_ratio_mu=0.80, night_ratio_mu=0.50),
    "printer": dict(n=25, bytes_mu=1.5e7, bytes_sigma=8.0e6, pkts_mu=9000, pkts_sigma=4000,
                      conns_mu=10, conns_sigma=4, dur_mu=20, dur_sigma=10, ports_mu=2, ports_sigma=1,
                      ips_mu=2, ips_sigma=1, tcp_ratio_mu=0.60, night_ratio_mu=0.05),
}

rows = []
for device_type, p in DEVICE_PROFILES.items():
    n = p["n"]
    total_bytes = rng.normal(p["bytes_mu"], p["bytes_sigma"], n).clip(min=1e5)
    total_packets = rng.normal(p["pkts_mu"], p["pkts_sigma"], n).clip(min=100)
    num_connections = rng.normal(p["conns_mu"], p["conns_sigma"], n).clip(min=1)
    avg_conn_duration_sec = rng.normal(p["dur_mu"], p["dur_sigma"], n).clip(min=0.5)
    unique_dst_ports = rng.normal(p["ports_mu"], p["ports_sigma"], n).clip(min=1)
    unique_dst_ips = rng.normal(p["ips_mu"], p["ips_sigma"], n).clip(min=1)
    tcp_ratio = rng.normal(p["tcp_ratio_mu"], 0.08, n).clip(0, 1)
    night_activity_ratio = rng.normal(p["night_ratio_mu"], 0.08, n).clip(0, 1)
    avg_packet_size = total_bytes / total_packets

    for i in range(n):
        rows.append(dict(
            device_id=f"{device_type}_{i:04d}",
            total_bytes=total_bytes[i],
            total_packets=int(total_packets[i]),
            avg_packet_size=avg_packet_size[i],
            num_connections=int(num_connections[i]),
            avg_conn_duration_sec=avg_conn_duration_sec[i],
            unique_dst_ports=int(unique_dst_ports[i]),
            unique_dst_ips=int(unique_dst_ips[i]),
            tcp_ratio=tcp_ratio[i],
            night_activity_ratio=night_activity_ratio[i],
            device_type=device_type,
        ))

df = pd.DataFrame(rows)
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Missing values: a handful of real-world-style gaps, concentrated in two columns.
missing_idx_ports = rng.choice(df.index, size=15, replace=False)
df.loc[missing_idx_ports, "unique_dst_ports"] = np.nan
missing_idx_night = rng.choice(df.index, size=10, replace=False)
df.loc[missing_idx_night, "night_activity_ratio"] = np.nan

# A few injected outliers (e.g. a laptop mid-download, a misbehaving camera) --
# plausible, not meant to be "the answer," just realistic noise to react to.
outlier_idx = rng.choice(df.index, size=4, replace=False)
df.loc[outlier_idx[:2], "total_bytes"] *= 6
df.loc[outlier_idx[2:], "num_connections"] *= 8

df.to_csv("traffic_data.csv", index=False)
print(f"Wrote traffic_data.csv with {len(df)} rows, {df['device_type'].nunique()} device types.")
print(df["device_type"].value_counts())

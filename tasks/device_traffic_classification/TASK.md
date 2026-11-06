# Mock task — Device classification from network traffic

Set a timer for 60 minutes before reading past this line. No AI coding assistant, no looking up the generator script. Treat this like you're in the room.

## Scenario
You work at a network intelligence company that helps ISPs understand what's connected to their subscribers' home networks. For each device seen on a sample of home networks, we've aggregated its traffic over a one-week window into a single row of summary statistics. We want to automatically identify what *type* of device each row represents, without the subscriber having to tell us.

## Data
`traffic_data.csv`, one row per device, columns:
- `device_id` — unique identifier (string, not a feature)
- `total_bytes` — total bytes transferred over the week
- `total_packets` — total packet count
- `avg_packet_size` — average bytes per packet
- `num_connections` — number of distinct connection sessions
- `avg_conn_duration_sec` — average duration of a connection session, in seconds
- `unique_dst_ports` — count of distinct destination ports contacted
- `unique_dst_ips` — count of distinct destination IPs contacted
- `tcp_ratio` — fraction of traffic that was TCP (vs UDP)
- `night_activity_ratio` — fraction of connections occurring 00:00-06:00
- `device_type` — label: one of `laptop`, `smart_tv`, `ip_camera`, `smart_speaker`, `smart_thermostat`, `printer`

## Task
1. Explore the data. Note anything that looks off (missing values, outliers, class balance).
2. Build a model to predict `device_type` from the traffic features.
3. Evaluate it properly, and be ready to explain *why* you chose that evaluation approach given the class distribution.
4. Identify which features matter most for the prediction, and whether that matches your intuition about these device types.
5. Prepare a short (5-bullet) summary as if you had 5 minutes to present this to the team: approach, headline result, one limitation, one thing you'd do with more time.

## Constraints
- Stick to the 60-minute budget. Stop at 60 minutes wherever you are and write the summary with what you have — that's part of the practice.
- Use `generate_data.py` only to produce the CSV first; don't re-read it during the task, it'll spoil the EDA.

## After
Come back and walk through your notebook/script and the 5-bullet summary — we'll review it the same way we've been going through the SQL practice.

+++
title = 'Remove Telemetry from Streamlit'
date = 2025-10-18T15:24:48-05:00
draft = false
tags = ['python','streamlit','telemetry']
summary = 'Disable telemetry in StreamLit especially for work projects.'
comments = true
+++

he first time you run streamlit, it will show a welcome message and ask you
for your email. There’s also some telemetry practices you should read about.
Briefly, they want to send some usage data to their servers when the streamlit
server runs. You can write a two-line configuration file that prevents this
telemetry from running:

```python
[browser]
gatherUsageStats = false
```

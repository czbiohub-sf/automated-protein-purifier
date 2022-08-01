# BUGS
1. Server does not signal availability after client completes protocol if client does not explicitly disconnect. This prevents a follow up connection to the device.
2. Logging appears to be destroyed before executing the contents in __del__() methods. Logging the destruction of ports would be convenient.

# CONSIDERATIONS
1. Include connection state model in client so that subsequent commands are not issued in the event of connection or hardware failure. Currently issues commands even when "Response not received." from server
2. Include pump duration in client command so that server knows when to terminate pumping. Alternatively, terminate pumping upon loss of connection identified via heartbeat.
3. Add logging config file for scripts so that all scripts follow same logging convention
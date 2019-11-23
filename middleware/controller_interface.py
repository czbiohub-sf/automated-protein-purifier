

# Psuedocode
#
# while connected:
#   if cmd in cmd_queue:
#       try:
#          send(P5100, cmd)
#          r = receive(P5200, 5s)
#       except Error:
#           warning reply not received
#           try:
#               send(P5100, cmd)
#               r = receive(P5200)
#           except:
#               error reply not received
#               disconnect?
#       t_last_cmd = now
#   if r not 'OK':
#       data_queue.append(r)
#   if now - t_last_cmd > 3:
#       send heartbeat

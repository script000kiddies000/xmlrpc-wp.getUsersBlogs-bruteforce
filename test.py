address = request.args.get("address")
cmd = "ping -c 1 %s" % address
subprocess.Popen(cmd, shell=True)

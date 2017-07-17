from datetime import datetime
ist=raw_input("Enter date and time in YYYY:MM::DD and HH:MM:SS format:")
diff='09:30:00'
fmt='%H:%M:%S'
est=datetime.strptime(ist,fmt)-datetime.strptime(diff,fmt)
print str(est)
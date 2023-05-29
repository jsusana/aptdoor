from datetime import datetime

def get_last_alert_time():
    with open('data/lastAlertSent.txt') as f:
        lines = f.readlines()
        if len(lines) <= 0:
            return 999
        
        last_sent = datetime.strptime(lines[0], '%m/%d/%y %H:%M:%S')
        return (datetime.now() - last_sent).total_seconds()

        
def set_last_alert_time(time):
    with open('data/lastAlertSent.txt', 'w') as f:
        f.write(time)

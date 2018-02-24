with open('booking-activity-part.html', 'r') as f:
    text = f.read()

with open('booking-activity-part.html', 'w+') as f:
    f.write(text.replace('\n', '').replace('\t', ''))
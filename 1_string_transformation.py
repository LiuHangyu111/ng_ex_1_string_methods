booking = "   EVT-2026 | alice_wong | Room-305 | 14:30 | alice.wong@UniMail.edu | VIP-VIP   "

event_code = booking.split('|')[0].strip()
name = booking.split('|')[1].strip()
room = booking.split('|')[2].strip()
time = booking.split('|')[3].strip()
email = booking.split('|')[4].strip()
vip_tag = booking.split('|')[5].strip()

name_formatted = name.replace('_', ' ').title().replace(' ', '_')

room_formatted = room.upper()

email_domain = email.split('@')[1].lower()

vip_count = vip_tag.count('VIP')

valid_event = event_code.startswith('EVT-') and len(event_code.split('-')[1]) == 4 and event_code.split('-')[1].isdigit()

valid_name = True
for c in name:
    if not (c.isalnum() or c == '_'):
        valid_name = False
valid_name = valid_name and '_' in name

valid_room = room_formatted.startswith('ROOM-') and len(room_formatted.split('-')[1]) == 3 and room_formatted.split('-')[1].isdigit()

valid_time = len(time) == 5 and time[2] == ':' and time[:2].isdigit() and time[3:].isdigit() and 0 <= int(time[:2]) < 24 and 0 <= int(time[3:]) < 60

valid_email = '@' in email and '.' in email.split('@')[1] and email.split('@')[0].replace('.', '').replace('_', '').isalnum()

print(f'Event code: {event_code}')
print(f'Name: {name_formatted}')
print(f'Room: {room_formatted}')
print(f'Time: {time}')
print(f'Email domain: {email_domain}')
print(f'VIP tag count: {vip_count}')
print(f'Valid event code: {valid_event}')
print(f'Valid username: {valid_name}')
print(f'Valid room: {valid_room}')
print(f'Valid time: {valid_time}')
print(f'Valid email: {valid_email}')
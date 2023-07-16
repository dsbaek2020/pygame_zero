
age = 13

solution = ['seoul', 'Seoul', 'SEOUL']  #list

print('Hello this is quiz game.')
answer = input('what is South Korea capital? --> ')

if answer == solution[0]:
    print('yes')
elif answer == solution[1]:
    print('good')
elif answer == solution[2]:
    print('nice')
else:
    print('no')


if answer == solution[0] or  answer == solution[1] \
   or answer == solution[2]:
    print('yes')
else :
    print('no')


import pgzrun

WIDTH = 1280
HEIGHT = 720

# make a quiz information by the list.


# draw button x 4, quiz text_box, time_box,
  # make rectangular * 6 by Rect class.
  # draw rect.fill_rect --> draw rect
  # draw rect.text --> draw text

# Make event for like interactive program.

# Make timer ex) 10 - 9 - 8 - 7 ... 1 - 0 ---> game over

# make variable -- > score






pgzrun.go()

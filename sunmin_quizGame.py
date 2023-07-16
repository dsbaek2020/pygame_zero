'''
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
'''

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

main_box = Rect(0, 0, 820, 240)
main_box.move_ip(50, 40)

timer_box = Rect(0, 0, 240, 240)
timer_box.move_ip(990, 40)

answer_box1 = Rect(0, 0, 495, 165)
answer_box1.move_ip(50, 358)

answer_box2 = Rect(0, 0, 495, 165)
answer_box2.move_ip(735, 358)

answer_box3 = Rect(0, 0, 495, 165)
answer_box3.move_ip(50, 538)

answer_box4 = Rect(0, 0, 495, 165)
answer_box4.move_ip(735, 538)

answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]


def draw():
    screen.fill("dim gray")
    screen.draw.filled_rect(main_box, "coral")
    screen.draw.filled_rect(timer_box, "coral")

    for box in answer_boxes:
        screen.draw.filled_rect(box, "orange")


pgzrun.go()
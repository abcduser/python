import turtle


def draw_my_shape(t_o, e_1, e_2, e_3, e_4, e_5, e_6, e_7, e_8):
    angle = 360 / 8

    t_o.forward(e_1)
    t_o.right(angle)
    t_o.forward(e_2)
    t_o.right(angle)
    t_o.forward(e_3)
    t_o.right(angle)
    t_o.forward(e_4)
    t_o.right(angle)
    t_o.forward(e_5)
    t_o.right(angle)
    t_o.forward(e_6)
    t_o.right(angle)
    t_o.forward(e_7)
    t_o.right(angle)
    t_o.forward(e_8)
    t_o.right(angle)


def main():
    t_obj = turtle.Pen()
    t_obj.color('red')

    ep_1 = int(input('Enter End Point 1'))
    ep_2 = int(input('Enter End Point 2'))
    ep_3 = int(input('Enter End Point 3'))
    ep_4 = int(input('Enter End Point 4'))
    ep_5 = int(input('Enter End Point 5'))
    ep_6 = int(input('Enter End Point 6'))
    ep_7 = int(input('Enter End Point 7'))
    ep_8 = int(input('Enter End Point 8'))

    draw_my_shape(t_obj, ep_1, ep_2, ep_3, ep_4, ep_5, ep_6, ep_7, ep_8)


main()

input()

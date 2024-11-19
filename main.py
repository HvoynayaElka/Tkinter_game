import tkinter
from PIL import Image, ImageTk
from textwrap import wrap


class SoggyRoom:
    def __init__(self, master, label_im, label_text, player):
        self.master = master
        self.label_im = label_im
        self.label_text = label_text
        self.player = player

        self.BigHall_button = tkinter.Label(self.master, borderwidth=0)
        self.BigHall_button.leave_im = ImageTk.PhotoImage(Image.open('bighall button leave.png'))
        self.BigHall_button.enter_im = ImageTk.PhotoImage(Image.open('bighall button enter.png'))
        make_binds(self.BigHall_button, self.BigHall_button.leave_im, self.BigHall_button.enter_im, self.go_to_big_hall)

        self.EastHall_button = tkinter.Label(self.master, borderwidth=0)
        self.EastHall_button.leave_im = ImageTk.PhotoImage(Image.open('east hall button leave.png'))
        self.EastHall_button.enter_im = ImageTk.PhotoImage(Image.open('east hall button enter.png'))
        make_binds(self.EastHall_button, self.EastHall_button.leave_im, self.EastHall_button.enter_im,
                   self.go_to_east_hall)

        self.WestHall_button = tkinter.Label(self.master, borderwidth=0)
        self.WestHall_button.leave_im = ImageTk.PhotoImage(Image.open('west hall button leave.png'))
        self.WestHall_button.enter_im = ImageTk.PhotoImage(Image.open('west hall button enter.png'))
        make_binds(self.WestHall_button, self.WestHall_button.leave_im, self.WestHall_button.enter_im,
                   self.go_to_west_hall)

        self.Key_button = tkinter.Label(self.master, borderwidth=0)
        self.Key_button.leave_im = ImageTk.PhotoImage(Image.open('pick up key leave.png'))
        self.Key_button.enter_im = ImageTk.PhotoImage(Image.open('pick up key enter.png'))
        make_binds(self.Key_button, self.Key_button.leave_im, self.Key_button.enter_im, self.pick_up_key)

        self.ok_button = tkinter.Button(self.master, text='OK', background='#330066',
                                        foreground='#D6DDE4', command=self.press_ok, font='Candra')
        self.label_info = tkinter.Label(self.master, text='you picked up a key!', borderwidth=15, background='#001933',
                                        foreground='#E0E0E0', font='Candra')

    def prepare_and_start(self):
        if 'key' not in self.player.inventory:
            self.master.im = ImageTk.PhotoImage(Image.open('soggy room.jpg'))
            self.label_im.config(image=self.master.im)
            self.Key_button.place(x=1579, y=787)
        else:
            self.master.im = ImageTk.PhotoImage(Image.open('soggy room 2.jpg'))
            self.label_im.config(image=self.master.im)
        new_text = ('You are in the Start room, there are parts of the endoskeleton everywhere.'
                    'Also there are strange monitors and colorful gifts. You see 3 corridors in front of you.')
        wrapped_text = text_wrap(new_text)
        self.label_text.config(text=wrapped_text)
        self.BigHall_button.place(x=825, y=330)
        self.EastHall_button.place(x=1690, y=485)
        self.WestHall_button.place(x=110, y=507)

    def go_to_big_hall(self):
        if not self.player.locked and not self.player.inventory_isOpen:
            self.buttons_destroy()
            BigHall(self.master, self.label_im, self.label_text, self.player).prepare_and_start()

    def go_to_east_hall(self):
        if not self.player.locked and not self.player.inventory_isOpen:
            self.buttons_destroy()
            EastHall(self.master, self.label_im, self.label_text, self.player).prepare_and_start()

    def go_to_west_hall(self):
        if not self.player.locked and not self.player.inventory_isOpen:
            self.buttons_destroy()
            WestHall(self.master, self.label_im, self.label_text, self.player).prepare_and_start()

    def pick_up_key(self):
        self.player.locked = True
        self.Key_button.destroy()
        self.label_info.place(x=900, y=550)  # need to change after adding right pictures.
        self.ok_button.place(x=970, y=600)  # need to change after adding right pictures.
        self.player.inventory.append('key')

    def press_ok(self):
        self.ok_button.destroy()
        self.label_info.destroy()
        self.player.locked = False
        self.buttons_destroy()
        SoggyRoom(self.master, self.label_im, self.label_text, self.player).prepare_and_start()

    def buttons_destroy(self):
        self.BigHall_button.destroy()
        self.EastHall_button.destroy()
        self.WestHall_button.destroy()
        self.Key_button.destroy()


class BigHall:
    def __init__(self, master, label_im, label_text, player):
        self.master = master
        self.label_im = label_im
        self.label_text = label_text
        self.player = player

        self.Scene_button = tkinter.Label(self.master, borderwidth=0)
        self.Scene_button.leave_im = ImageTk.PhotoImage(Image.open('scene button leave.png'))
        self.Scene_button.enter_im = ImageTk.PhotoImage(Image.open('scene button enter.png'))
        make_binds(self.Scene_button, self.Scene_button.leave_im, self.Scene_button.enter_im,
                   self.go_to_scene)

        self.Corridor_button = tkinter.Label(self.master, borderwidth=0)
        self.Corridor_button.leave_im = ImageTk.PhotoImage(Image.open('corridor button leave.png'))
        self.Corridor_button.enter_im = ImageTk.PhotoImage(Image.open('corridor button enter.png'))
        make_binds(self.Corridor_button, self.Corridor_button.leave_im, self.Corridor_button.enter_im,
                   self.go_to_corridor)

        self.SoggyRoom_button = tkinter.Label(self.master, borderwidth=0)
        self.SoggyRoom_button.leave_im = ImageTk.PhotoImage(Image.open('soggy room button leave.png'))
        self.SoggyRoom_button.enter_im = ImageTk.PhotoImage(Image.open('soggy room button enter.png'))
        make_binds(self.SoggyRoom_button, self.SoggyRoom_button.leave_im, self.SoggyRoom_button.enter_im,
                   self.go_to_soggy_room)

        self.Back_room_button = tkinter.Label(self.master, borderwidth=0)
        self.Back_room_button.leave_im = ImageTk.PhotoImage(Image.open('back room button leave.png'))
        self.Back_room_button.enter_im = ImageTk.PhotoImage(Image.open('back room button enter.png'))
        make_binds(self.Back_room_button, self.Back_room_button.leave_im, self.Back_room_button.enter_im,
                   self.go_to_back_room)

    def prepare_and_start(self):
        self.master.im = ImageTk.PhotoImage(Image.open('big hall.jpg'))
        self.label_im.config(image=self.master.im)
        new_text = ("You have come to a huge hall. It's very dark in here. In front of you is a stage covered with curtains. To your left there is a passage from which the light comes. There is a door next to the slot machine.")
        wrapped_text = text_wrap(new_text)
        self.label_text.config(text=wrapped_text)
        self.SoggyRoom_button.place(x=840, y=835)
        self.Corridor_button.place(x=30, y=435)
        self.Scene_button.place(x=515, y=430)  # need to change after adding right pictures.
        self.Back_room_button.place(x=1430, y=435)

    def go_to_soggy_room(self):
        if not self.player.locked and not self.player.inventory_isOpen:
            self.buttons_destroy()
            SoggyRoom(self.master, self.label_im, self.label_text, self.player).prepare_and_start()

    def go_to_corridor(self):
        if not self.player.locked and not self.player.inventory_isOpen:
            self.buttons_destroy()
            Corridor(self.master, self.label_im, self.label_text, self.player).prepare_and_start()

    def go_to_scene(self):
        if not self.player.locked and not self.player.inventory_isOpen:
            self.buttons_destroy()
            Scene(self.master, self.label_im, self.label_text, self.player).prepare_and_start()

    def go_to_back_room(self):
        if not self.player.locked and not self.player.inventory_isOpen:
            self.buttons_destroy()
            BackRoom(self.master, self.label_im, self.label_text, self.player).prepare_and_start()

    def buttons_destroy(self):
        self.SoggyRoom_button.destroy()
        self.Corridor_button.destroy()
        self.Scene_button.destroy()
        self.Back_room_button.destroy()


class EastHall:
    def __init__(self, master, label_im, label_text, player):
        self.master = master
        self.label_im = label_im
        self.label_text = label_text
        self.player = player

        self.SoggyRoom_button = tkinter.Label(self.master, borderwidth=0)
        self.SoggyRoom_button.leave_im = ImageTk.PhotoImage(Image.open('soggy room button leave 2.png'))
        self.SoggyRoom_button.enter_im = ImageTk.PhotoImage(Image.open('soggy room button enter 2.png'))
        make_binds(self.SoggyRoom_button, self.SoggyRoom_button.leave_im, self.SoggyRoom_button.enter_im,
                   self.go_to_soggy_room)

    def prepare_and_start(self):
        self.master.im = ImageTk.PhotoImage(Image.open('east hall.jpg'))
        self.label_im.config(image=self.master.im)
        new_text = ("You have come to a strange room, colorful balls are lying everywhere,"
                    "and three clocks are hanging on the wall, red numbers are hanging under the clock...")
        wrapped_text = text_wrap(new_text)
        self.label_text.config(text=wrapped_text)
        self.SoggyRoom_button.place(x=575, y=730)

    def go_to_soggy_room(self):
        if not self.player.locked and not self.player.inventory_isOpen:
            self.SoggyRoom_button.destroy()
            SoggyRoom(self.master, self.label_im, self.label_text, self.player).prepare_and_start()


class WestHall:
    def __init__(self, master, label_im, label_text, player):
        self.master = master
        self.label_im = label_im
        self.label_text = label_text
        self.player = player

        self.SoggyRoom_button = tkinter.Label(self.master, borderwidth=0)
        self.SoggyRoom_button.leave_im = ImageTk.PhotoImage(Image.open('soggy room button leave 3.png'))
        self.SoggyRoom_button.enter_im = ImageTk.PhotoImage(Image.open('soggy room button enter 3.png'))
        make_binds(self.SoggyRoom_button, self.SoggyRoom_button.leave_im, self.SoggyRoom_button.enter_im,
                   self.go_to_soggy_room)

        self.Storeroom_button = tkinter.Label(self.master, borderwidth=0)
        self.Storeroom_button.leave_im = ImageTk.PhotoImage(Image.open('storeroom button leave 2.png'))
        self.Storeroom_button.enter_im = ImageTk.PhotoImage(Image.open('storeroom button enter 2.png'))
        make_binds(self.Storeroom_button, self.Storeroom_button.leave_im, self.Storeroom_button.enter_im,
                   self.go_to_storeroom)

        self.PickUpPart2 = tkinter.Label(self.master, borderwidth=0)
        self.PickUpPart2.leave_im = ImageTk.PhotoImage(Image.open('pick up part2 leave.png'))
        self.PickUpPart2.enter_im = ImageTk.PhotoImage(Image.open('pick up part2 enter.png'))
        make_binds(self.PickUpPart2, self.PickUpPart2.leave_im, self.PickUpPart2.enter_im,
                   self.pick_up_part2)

        self.ok_button = tkinter.Button(self.master, text='OK', background='#330066',
                                        foreground='#D6DDE4', command=self.press_ok, font='Candra')
        self.label_info = tkinter.Label(self.master, text='you picked up a part!',
                                        borderwidth=15, background='#001933', foreground='#E0E0E0', font='Candra')

    def prepare_and_start(self):
        if ('part 3' not in self.player.inventory and 'eye' not in self.player.inventory and 'green number'
                not in self.player.inventory):
            self.master.im = ImageTk.PhotoImage(Image.open('west hall.jpg'))
            self.label_im.config(image=self.master.im)
            self.PickUpPart2.place(x=536, y=205)
        else:
            self.master.im = ImageTk.PhotoImage(Image.open('west hall(2).jpg'))
            self.label_im.config(image=self.master.im)
        new_text = ("You came to a room with rusty pipes. There is an unusual poster hanging in front of you,"
                    "and there is also a passage.")
        wrapped_text = text_wrap(new_text)
        self.label_text.config(text=wrapped_text)
        self.SoggyRoom_button.place(x=1160, y=760)
        self.Storeroom_button.place(x=900, y=363)

    def go_to_soggy_room(self):
        if not self.player.locked and not self.player.inventory_isOpen:
            self.buttons_destroy()
            SoggyRoom(self.master, self.label_im, self.label_text, self.player).prepare_and_start()

    def go_to_storeroom(self):
        if not self.player.locked and not self.player.inventory_isOpen:
            self.buttons_destroy()
            Storeroom(self.master, self.label_im, self.label_text, self.player).prepare_and_start()

    def buttons_destroy(self):
        self.SoggyRoom_button.destroy()
        self.Storeroom_button.destroy()
        self.PickUpPart2.destroy()

    def pick_up_part2(self):
        self.player.locked = True
        self.PickUpPart2.destroy()
        self.label_info.place(x=900, y=300)
        self.ok_button.place(x=955, y=350)
        self.player.inventory.append('part 3')

    def press_ok(self):
        self.ok_button.destroy()
        self.label_info.destroy()
        self.player.locked = False
        self.buttons_destroy()
        WestHall(self.master, self.label_im, self.label_text, self.player).prepare_and_start()


class Storeroom:
    def __init__(self, master, label_im, label_text, player):
        self.master = master
        self.label_im = label_im
        self.label_text = label_text
        self.player = player

        self.WestHall_button = tkinter.Label(self.master, borderwidth=0)
        self.WestHall_button.leave_im = ImageTk.PhotoImage(Image.open('west hall button leave 2.png'))
        self.WestHall_button.enter_im = ImageTk.PhotoImage(Image.open('west hall button enter 2.png'))
        make_binds(self.WestHall_button, self.WestHall_button.leave_im, self.WestHall_button.enter_im,
                   self.go_to_west_hall)

        self.Corridor_button = tkinter.Label(self.master, borderwidth=0)
        self.Corridor_button.leave_im = ImageTk.PhotoImage(Image.open('corridor button leave 2.png'))
        self.Corridor_button.enter_im = ImageTk.PhotoImage(Image.open('corridor button enter 2.png'))
        make_binds(self.Corridor_button, self.Corridor_button.leave_im, self.Corridor_button.enter_im,
                   self.go_to_corridor)

        self.Get_number_button = tkinter.Label(self.master, borderwidth=0)
        self.Get_number_button.leave_im = ImageTk.PhotoImage(Image.open('pinguin button leave.png'))
        self.Get_number_button.enter_im = ImageTk.PhotoImage(Image.open('pinguin button enter.png'))
        make_binds(self.Get_number_button, self.Get_number_button.leave_im, self.Get_number_button.enter_im,
                   self.get_number)

        self.label_info = tkinter.Label(self.master, borderwidth=15, background='#001933',
                                        foreground='#E0E0E0', font='Candra')
        self.ok_button = tkinter.Button(self.master, text='OK', background='#330066',
                                        foreground='#D6DDE4', command=self.press_ok, font='Candra')

    def prepare_and_start(self):
        if 'green number' not in self.player.inventory:
            self.master.im = ImageTk.PhotoImage(Image.open('storeroom.jpg'))
            self.label_im.config(image=self.master.im)
            self.Get_number_button.place(x=625, y=615)
        else:
            self.master.im = ImageTk.PhotoImage(Image.open('storeroom 2.jpg'))
            self.label_im.config(image=self.master.im)
        new_text = ("You came to the storeroom. Your attention was attracted by a strange toy without an eye, standing on one of the shelves. There is a passage in front of you.")
        wrapped_text = text_wrap(new_text)
        self.label_text.config(text=wrapped_text)
        self.WestHall_button.place(x=1220, y=695)
        self.Corridor_button.place(x=1105, y=370)

    def go_to_west_hall(self):
        if not self.player.locked and not self.player.inventory_isOpen:
            self.buttons_destroy()
            WestHall(self.master, self.label_im, self.label_text, self.player).prepare_and_start()

    def go_to_corridor(self):
        if not self.player.locked and not self.player.inventory_isOpen:
            self.buttons_destroy()
            Corridor(self.master, self.label_im, self.label_text, self.player).prepare_and_start()

    def buttons_destroy(self):
        self.WestHall_button.destroy()
        self.Corridor_button.destroy()
        self.Get_number_button.destroy()

    def get_number(self):
        if 'eye' not in self.player.inventory:
            self.label_info.config(text='A strange toy without an eye...')
        else:
            self.label_info.config(text='You got a number!')
            self.player.inventory.append('green number')
            self.player.inventory.remove('eye')
        self.label_info.place(x=900, y=300)  # need to change after adding right pictures.
        self.ok_button.place()
        self.ok_button.place(x=955, y=350)  # need to change after adding right pictures.
        self.player.locked = True

    def press_ok(self):
        self.ok_button.destroy()
        self.label_info.destroy()
        self.player.locked = False
        self.buttons_destroy()
        Storeroom(self.master, self.label_im, self.label_text, self.player).prepare_and_start()


class Corridor:
    def __init__(self, master, label_im, label_text, player):
        self.master = master
        self.label_im = label_im
        self.label_text = label_text
        self.player = player

        self.Storeroom_button = tkinter.Label(self.master, borderwidth=0)
        self.Storeroom_button.leave_im = ImageTk.PhotoImage(Image.open('storeroom button leave.png'))
        self.Storeroom_button.enter_im = ImageTk.PhotoImage(Image.open('storeroom button enter.png'))
        make_binds(self.Storeroom_button, self.Storeroom_button.leave_im, self.Storeroom_button.enter_im,
                   self.go_to_storeroom)

        self.Corner_room_button = tkinter.Label(self.master, borderwidth=0)
        self.Corner_room_button.leave_im = ImageTk.PhotoImage(Image.open('corner room button leave.png'))
        self.Corner_room_button.enter_im = ImageTk.PhotoImage(Image.open('corner room button enter.png'))
        make_binds(self.Corner_room_button, self.Corner_room_button.leave_im, self.Corner_room_button.enter_im,
                   self.go_to_corner_room)

        self.BigHall_button = tkinter.Label(self.master, borderwidth=0)
        self.BigHall_button.leave_im = ImageTk.PhotoImage(Image.open('bighall button leave 2.png'))
        self.BigHall_button.enter_im = ImageTk.PhotoImage(Image.open('bighall button enter 2.png'))
        make_binds(self.BigHall_button, self.BigHall_button.leave_im, self.BigHall_button.enter_im, self.go_to_big_hall)

        self.Pick_up_button = tkinter.Label(self.master, borderwidth=0)
        self.Pick_up_button.leave_im = ImageTk.PhotoImage(Image.open('Pick up blue leave.png'))
        self.Pick_up_button.enter_im = ImageTk.PhotoImage(Image.open('Pick up blue enter.png'))
        make_binds(self.Pick_up_button, self.Pick_up_button.leave_im, self.Pick_up_button.enter_im,
                   self.pick_up_blue_number)

        self.ok_button = tkinter.Button(self.master, text='OK', background='#330066',
                                        foreground='#D6DDE4', command=self.press_ok, font='Candra')
        self.label_info = tkinter.Label(self.master, text='you picked up a number!', borderwidth=15,
                                        background='#001933', foreground='#E0E0E0', font='Candra')

    def prepare_and_start(self):
        if 'blue number' not in self.player.inventory:
            self.master.im = ImageTk.PhotoImage(Image.open('corridor.jpg'))
            self.label_im.config(image=self.master.im)
            self.Pick_up_button.place(x=565, y=840)
        else:
            self.master.im = ImageTk.PhotoImage(Image.open('corridor 2.jpg'))
            self.label_im.config(image=self.master.im)
        new_text = ("You have come to a strange corridor. there are passageways to your left and right."
                    "A blue book is lying on the floor...")
        wrapped_text = text_wrap(new_text)
        self.label_text.config(text=wrapped_text)
        self.Storeroom_button.place(x=1030, y=810)
        self.Corner_room_button.place(x=200, y=330)
        self.BigHall_button.place(x=1415, y=330)

    def go_to_storeroom(self):
        if not self.player.locked and not self.player.inventory_isOpen:
            self.buttons_destroy()
            Storeroom(self.master, self.label_im, self.label_text, self.player).prepare_and_start()

    def go_to_corner_room(self):
        if not self.player.locked and not self.player.inventory_isOpen:
            self.buttons_destroy()
            CornerRoom(self.master, self.label_im, self.label_text, self.player).prepare_and_start()

    def go_to_big_hall(self):
        if not self.player.locked and not self.player.inventory_isOpen:
            self.buttons_destroy()
            BigHall(self.master, self.label_im, self.label_text, self.player).prepare_and_start()

    def buttons_destroy(self):
        self.Storeroom_button.destroy()
        self.Corner_room_button.destroy()
        self.BigHall_button.destroy()
        self.Pick_up_button.destroy()

    def pick_up_blue_number(self):
        self.player.locked = True
        self.Pick_up_button.destroy()
        self.label_info.place(x=900, y=550)
        self.ok_button.place(x=980, y=600)
        self.player.inventory.append('blue number')

    def press_ok(self):
        self.ok_button.destroy()
        self.label_info.destroy()
        self.player.locked = False
        self.buttons_destroy()
        Corridor(self.master, self.label_im, self.label_text, self.player).prepare_and_start()


class CornerRoom:
    def __init__(self, master, label_im, label_text, player):
        self.master = master
        self.label_im = label_im
        self.label_text = label_text
        self.player = player

        self.Corridor_button = tkinter.Label(self.master, borderwidth=0)
        self.Corridor_button.leave_im = ImageTk.PhotoImage(Image.open('corner room button leave 2.png'))
        self.Corridor_button.enter_im = ImageTk.PhotoImage(Image.open('corner room button enter 2.png'))
        make_binds(self.Corridor_button, self.Corridor_button.leave_im, self.Corridor_button.enter_im,
                   self.go_to_corridor)

        self.Pick_up_button = tkinter.Label(self.master, borderwidth=0)
        self.Pick_up_button.leave_im = ImageTk.PhotoImage(Image.open('pick up part1 button leave.png'))
        self.Pick_up_button.enter_im = ImageTk.PhotoImage(Image.open('pick up part1 button enter.png'))
        make_binds(self.Pick_up_button, self.Pick_up_button.leave_im, self.Pick_up_button.enter_im,
                   self.pick_up_part2)

        self.ok_button = tkinter.Button(self.master, text='OK', background='#330066',
                                        foreground='#D6DDE4', command=self.press_ok, font='Candra')
        self.label_info = tkinter.Label(self.master, text='you picked up a part!', borderwidth=15,
                                        background='#001933', foreground='#E0E0E0', font='Candra')

    def prepare_and_start(self):
        if ('part 1' not in self.player.inventory and 'eye' not in self.player.inventory and 'green number'
                not in self.player.inventory):
            self.master.im = ImageTk.PhotoImage(Image.open('corner room.jpg'))
            self.label_im.config(image=self.master.im)
            self.Pick_up_button.place(x=570, y=685)
        else:
            self.master.im = ImageTk.PhotoImage(Image.open('corner room 2.jpg'))
            self.label_im.config(image=self.master.im)
        new_text = ("You have come to a room with 'parts and service' written on the door. Almost no light gets here."
                    "In front of you are a clock and a large animatronic, next to which there is something... "
                    "I don't think it's worth staying here...")
        wrapped_text = text_wrap(new_text)
        self.label_text.config(text=wrapped_text)
        self.Corridor_button.place(x=1375, y=550)

    def go_to_corridor(self):
        if not self.player.locked and not self.player.inventory_isOpen:
            self.Corridor_button.destroy()
            self.Pick_up_button.destroy()
            Corridor(self.master, self.label_im, self.label_text, self.player).prepare_and_start()

    def pick_up_part2(self):
        self.player.locked = True
        self.Pick_up_button.destroy()
        self.label_info.place(x=900, y=300)
        self.ok_button.place(x=955, y=350)
        self.player.inventory.append('part 1')

    def press_ok(self):
        self.ok_button.destroy()
        self.label_info.destroy()
        self.player.locked = False
        self.Corridor_button.destroy()
        CornerRoom(self.master, self.label_im, self.label_text, self.player).prepare_and_start()


class Scene:
    def __init__(self, master, label_im, label_text, player):
        self.master = master
        self.label_im = label_im
        self.label_text = label_text
        self.player = player

        self.BigHall_button = tkinter.Label(self.master, borderwidth=0)
        self.BigHall_button.leave_im = ImageTk.PhotoImage(Image.open('bighall button leave 4.png'))
        self.BigHall_button.enter_im = ImageTk.PhotoImage(Image.open('bighall button enter 4.png'))
        make_binds(self.BigHall_button, self.BigHall_button.leave_im, self.BigHall_button.enter_im,
                   self.go_to_big_hall)

        self.Basement_button = tkinter.Label(self.master, borderwidth=0)
        self.Basement_button.leave_im = ImageTk.PhotoImage(Image.open('basement button leave.png'))
        self.Basement_button.enter_im = ImageTk.PhotoImage(Image.open('basement button enter.png'))
        make_binds(self.Basement_button, self.Basement_button.leave_im, self.Basement_button.enter_im,
                   self.go_to_basement)

    def prepare_and_start(self):
        self.master.im = ImageTk.PhotoImage(Image.open('scene.jpg'))
        self.label_im.config(image=self.master.im)
        new_text = ("You have entered the stage. It's very dark in here. There's a door in front of you."
                    "There are strange numbers of different colors hanging next to it.")
        wrapped_text = text_wrap(new_text)
        self.label_text.config(text=wrapped_text)
        self.BigHall_button.place(x=1140, y=785)
        self.Basement_button.place(x=510, y=180)

    def go_to_big_hall(self):
        if not self.player.locked and not self.player.inventory_isOpen:
            self.buttons_destroy()
            BigHall(self.master, self.label_im, self.label_text, self.player).prepare_and_start()

    def go_to_basement(self):
        if not self.player.locked and not self.player.inventory_isOpen:
            self.buttons_destroy()
            Basement(self.master, self.label_im, self.label_text, self.player).prepare_and_start()

    def buttons_destroy(self):
        self.BigHall_button.destroy()
        self.Basement_button.destroy()


class Basement:
    def __init__(self, master, label_im, label_text, player):
        self.master = master
        self.label_im = label_im
        self.label_text = label_text
        self.player = player
        self.right_code = '5379'
        self.player_code = ''

        self.Scene_button = tkinter.Label(self.master, borderwidth=0)
        self.Scene_button.leave_im = ImageTk.PhotoImage(Image.open('scene button leave 2.png'))
        self.Scene_button.enter_im = ImageTk.PhotoImage(Image.open('scene button enter 2.png'))
        make_binds(self.Scene_button, self.Scene_button.leave_im, self.Scene_button.enter_im,
                   self.go_to_scene)

        self.label_console = tkinter.Label(self.master, height=11, width=15, font=("Helvetica", 14),
                                           background='#AE8455', borderwidth=5, relief="ridge")
        self.label_code = tkinter.Label(self.master, font=("Helvetica", 14), background='#001d18',
                                        foreground='#D6DDE4', borderwidth=5, relief="ridge", width=12)

        self.enter_code_button = tkinter.Label(self.master, borderwidth=0)
        self.enter_code_button.leave_im = ImageTk.PhotoImage(Image.open('enter code button leave.png'))
        self.enter_code_button.enter_im = ImageTk.PhotoImage(Image.open('enter code button enter.png'))
        make_binds(self.enter_code_button, self.enter_code_button.leave_im, self.enter_code_button.enter_im,
                   self.open_console)

        self.ok_button = tkinter.Button(self.master, text='OK', background='#A8A29C',
                                        foreground='#1C1A18', width=5, command=self.press_ok)
        self.button_1 = tkinter.Button(self.master, text='1', background='#A8A29C',
                                       foreground='#1C1A18', width=5, command=lambda: self.enter_num('1'))
        self.button_2 = tkinter.Button(self.master, text='2', background='#A8A29C',
                                       foreground='#1C1A18', width=5, command=lambda: self.enter_num('2'))
        self.button_3 = tkinter.Button(self.master, text='3', background='#A8A29C',
                                       foreground='#1C1A18', width=5, command=lambda: self.enter_num('3'))
        self.button_4 = tkinter.Button(self.master, text='4', background='#A8A29C',
                                       foreground='#1C1A18', width=5, command=lambda: self.enter_num('4'))
        self.button_5 = tkinter.Button(self.master, text='5', background='#A8A29C',
                                       foreground='#1C1A18', width=5, command=lambda: self.enter_num('5'))
        self.button_6 = tkinter.Button(self.master, text='6', background='#A8A29C',
                                       foreground='#1C1A18', width=5, command=lambda: self.enter_num('6'))
        self.button_7 = tkinter.Button(self.master, text='7', background='#A8A29C',
                                       foreground='#1C1A18', width=5, command=lambda: self.enter_num('7'))
        self.button_8 = tkinter.Button(self.master, text='8', background='#A8A29C',
                                       foreground='#1C1A18', width=5, command=lambda: self.enter_num('8'))
        self.button_9 = tkinter.Button(self.master, text='9', background='#A8A29C',
                                       foreground='#1C1A18', width=5, command=lambda: self.enter_num('9'))
        self.button_0 = tkinter.Button(self.master, text='0', background='#A8A29C',
                                       foreground='#1C1A18', width=5, command=lambda: self.enter_num('0'))
        self.go_forward_button = tkinter.Button(self.master, text='Go forward', width=15, background='#A22C53',
                                                foreground='#D6DDE4', command=self.go_forward)
        self.go_forward_button = tkinter.Label(self.master, borderwidth=0)
        self.go_forward_button.leave_im = ImageTk.PhotoImage(Image.open('go forward button leave.png'))
        self.go_forward_button.enter_im = ImageTk.PhotoImage(Image.open('go forward button enter.png'))
        make_binds(self.go_forward_button, self.go_forward_button.leave_im, self.go_forward_button.enter_im,
                   self.go_forward)

    def prepare_and_start(self):
        if not self.player.access_to_exit:
            self.master.im = ImageTk.PhotoImage(Image.open('basement.jpg'))
            self.label_im.config(image=self.master.im)
            self.enter_code_button.place(x=950, y=515)
        else:
            self.master.im = ImageTk.PhotoImage(Image.open('basement2.jpg'))  # change later
            self.label_im.config(image=self.master.im)
            self.go_forward_button.place(x=1093, y=433)
        new_text = ("You got into the basement. In front of you is a closed metal door next to which there is a panel"
                    "for entering a password. Maybe if you have a password, you could leave.")
        wrapped_text = text_wrap(new_text)
        self.label_text.config(text=wrapped_text)
        self.Scene_button.place(x=580, y=825)

    def check_code(self):
        if len(self.player_code) == 4:
            if self.right_code == self.player_code:
                self.player.access_to_exit = True
                self.label_code.configure(text=self.player_code, foreground='green')
                self.ok_button.place(x=1000, y=650)
            else:
                self.label_code.configure(text=self.player_code, foreground='red')
                self.ok_button.place(x=1000, y=650)

    def enter_num(self, num):
        if len(self.player_code) != 4:
            self.player_code += num
            self.label_code.configure(text=self.player_code)
            self.check_code()
        elif len(self.player_code) == 4:
            self.check_code()

    def press_ok(self):
        self.player_code = ''
        self.destroy_buttons()
        self.label_code.destroy()
        self.label_console.destroy()
        self.player.locked = False
        Basement(self.master, self.label_im, self.label_text, self.player).prepare_and_start()

    def destroy_buttons(self):
        self.button_1.destroy()
        self.button_2.destroy()
        self.button_3.destroy()
        self.button_4.destroy()
        self.button_5.destroy()
        self.button_6.destroy()
        self.button_7.destroy()
        self.button_8.destroy()
        self.button_9.destroy()
        self.button_0.destroy()
        self.enter_code_button.destroy()
        self.Scene_button.destroy()
        self.ok_button.destroy()
        self.go_forward_button.destroy()

    def go_to_scene(self):
        if not self.player.locked and not self.player.inventory_isOpen:
            self.destroy_buttons()
            Scene(self.master, self.label_im, self.label_text, self.player).prepare_and_start()

    def go_forward(self):
        if not self.player.locked and not self.player.inventory_isOpen:
            self.destroy_buttons()
            TheEnd(self.master, self.label_im, self.label_text, self.player).prepare_and_start()

    def open_console(self):
        self.player.locked = True
        self.enter_code_button.destroy()
        self.label_console.place(x=884, y=440)
        self.label_code.place(x=902, y=450)
        self.button_1.place(x=900, y=500)
        self.button_2.place(x=950, y=500)
        self.button_3.place(x=1000, y=500)
        self.button_4.place(x=900, y=550)
        self.button_5.place(x=950, y=550)
        self.button_6.place(x=1000, y=550)
        self.button_7.place(x=900, y=600)
        self.button_8.place(x=950, y=600)
        self.button_9.place(x=1000, y=600)
        self.button_0.place(x=950, y=650)


class BackRoom:
    def __init__(self, master, label_im, label_text, player):
        self.master = master
        self.label_im = label_im
        self.label_text = label_text
        self.player = player

        self.BigHall_button = tkinter.Label(self.master, borderwidth=0)
        self.BigHall_button.leave_im = ImageTk.PhotoImage(Image.open('bighall button leave 3.png'))
        self.BigHall_button.enter_im = ImageTk.PhotoImage(Image.open('bighall button enter 3.png'))
        make_binds(self.BigHall_button, self.BigHall_button.leave_im, self.BigHall_button.enter_im, self.go_to_big_hall)

        self.Secret_room_button = tkinter.Label(self.master, borderwidth=0)
        self.Secret_room_button.leave_im = ImageTk.PhotoImage(Image.open('secret room button leave.png'))
        self.Secret_room_button.enter_im = ImageTk.PhotoImage(Image.open('secret room button enter.png'))
        make_binds(self.Secret_room_button, self.Secret_room_button.leave_im, self.Secret_room_button.enter_im,
                   self.go_to_secret_room)

        self.ok_button = tkinter.Button(self.master, text='OK', background='#330066',
                                        foreground='#D6DDE4', command=self.press_ok, font='Candra')
        self.label_info = tkinter.Label(self.master, borderwidth=15,
                                        background='#001933', foreground='#E0E0E0', font='Candra')

        self.eye_button = tkinter.Button(self.master, text='Pick up', width=15, background='#A22C53',
                                         foreground='#D6DDE4', command=self.pick_up_eye)
        self.eye_button = tkinter.Label(self.master, borderwidth=0)
        self.eye_button.leave_im = ImageTk.PhotoImage(Image.open('pick up eye button leave.png'))
        self.eye_button.enter_im = ImageTk.PhotoImage(Image.open('pick up eye button enter.png'))
        make_binds(self.eye_button, self.eye_button.leave_im, self.eye_button.enter_im,
                   self.pick_up_eye)

    def prepare_and_start(self):
        if 'eye' not in self.player.inventory and 'green number' not in self.player.inventory:
            self.master.im = ImageTk.PhotoImage(Image.open('back room.jpg'))
            self.label_im.config(image=self.master.im)
            self.eye_button.place(x=580, y=360)
        else:
            self.master.im = ImageTk.PhotoImage(Image.open('back room(all parts).jpg'))
            self.label_im.config(image=self.master.im)
        new_text = ("You got into a room with a bunch of spare parts. There is a strange puzzle on the table, perhaps "
                    "if you collect it you will get something... There is an unsigned door in front of you, "
                    "next to which there is an endoskeleton.")
        wrapped_text = text_wrap(new_text)
        self.label_text.config(text=wrapped_text)
        if 'key' not in self.player.inventory:
            make_binds(self.Secret_room_button, way=self.warning)
        else:
            if not self.player.access_to_secret_room:
                make_binds(self.Secret_room_button, way=self.warning)
            else:
                make_binds(self.Secret_room_button, way=self.go_to_secret_room)
        self.Secret_room_button.place(x=1075, y=390)
        self.BigHall_button.place(x=1675, y=185)

    def go_to_big_hall(self):
        if not self.player.locked and not self.player.inventory_isOpen:
            self.destroy_button()
            BigHall(self.master, self.label_im, self.label_text, self.player).prepare_and_start()

    def go_to_secret_room(self):
        if not self.player.locked and not self.player.inventory_isOpen:
            self.destroy_button()
            SecretRoom(self.master, self.label_im, self.label_text, self.player).prepare_and_start()

    def destroy_button(self):
        self.BigHall_button.destroy()
        self.Secret_room_button.destroy()
        self.eye_button.destroy()

    def warning(self):
        if not self.player.locked:
            if 'key' not in self.player.inventory:
                self.label_info.config(text='The door is locked.')
            else:
                self.label_info.config(text='You have successfully unlocked the door!')
                self.player.access_to_secret_room = True
            self.label_info.place(x=900, y=300)
            self.ok_button.place(x=955, y=350)
            self.player.locked = True

    def press_ok(self):
        self.ok_button.destroy()
        self.label_info.destroy()
        self.player.locked = False
        self.destroy_button()
        BackRoom(self.master, self.label_im, self.label_text, self.player).prepare_and_start()

    def open_secret_room(self):
        self.warning()
        self.player.access_to_secret_room = True

    def pick_up_eye(self):
        if not self.player.locked:
            self.player.locked = True
            if ('part 1' in self.player.inventory and 'part 2' in self.player.inventory and
                    'part 3' in self.player.inventory):
                self.label_info.config(text='You got a strange thing. It looks like an eye...')
                self.player.inventory.append('eye')
                self.player.inventory.remove('part 1')
                self.player.inventory.remove('part 2')
                self.player.inventory.remove('part 3')

            else:
                self.label_info.config(text='There are 3 parts missing here...')
            self.label_info.place(x=900, y=300)
            self.ok_button.place(x=1000, y=350)


class SecretRoom:
    def __init__(self, master, label_im, label_text, player):
        self.master = master
        self.label_im = label_im
        self.label_text = label_text
        self.player = player

        self.Back_room_button = tkinter.Label(self.master, borderwidth=0)
        self.Back_room_button.leave_im = ImageTk.PhotoImage(Image.open('back room button leave 2.png'))
        self.Back_room_button.enter_im = ImageTk.PhotoImage(Image.open('back room button enter 2.png'))
        make_binds(self.Back_room_button, self.Back_room_button.leave_im, self.Back_room_button.enter_im,
                   self.go_to_back_room)

        self.part3_button = tkinter.Label(self.master, borderwidth=0)
        self.part3_button.leave_im = ImageTk.PhotoImage(Image.open('pick up part3 button leave.png'))
        self.part3_button.enter_im = ImageTk.PhotoImage(Image.open('pick up part3 button enter.png'))
        make_binds(self.part3_button, self.part3_button.leave_im, self.part3_button.enter_im,
                   self.pick_up_part3)

        self.ok_button = tkinter.Button(self.master, text='OK', background='#330066',
                                        foreground='#D6DDE4', command=self.press_ok, font='Candra')
        self.label_info = tkinter.Label(self.master, text='you picked up a part!', borderwidth=15,
                                        background='#001933', foreground='#E0E0E0', font='Candra')

    def prepare_and_start(self):
        if ('part 2' not in self.player.inventory and 'eye' not in self.player.inventory and 'green number'
                not in self.player.inventory):
            self.master.im = ImageTk.PhotoImage(Image.open('secret room.jpg'))
            self.label_im.config(image=self.master.im)
            self.part3_button.place(x=360, y=510)
        else:
            self.master.im = ImageTk.PhotoImage(Image.open('secret room 2.jpg'))
            self.label_im.config(image=self.master.im)
        new_text = ("You have come to the office. There is a strange mask under the table."
                    "Perhaps you can find a security guard in this place.")
        wrapped_text = text_wrap(new_text)
        self.label_text.config(text=wrapped_text)
        self.Back_room_button.place(x=1100, y=780)

    def go_to_back_room(self):
        if not self.player.locked and not self.player.inventory_isOpen:
            self.Back_room_button.destroy()
            self.part3_button.destroy()
            BackRoom(self.master, self.label_im, self.label_text, self.player).prepare_and_start()

    def pick_up_part3(self):
        self.player.locked = True
        self.part3_button.destroy()
        self.label_info.place(x=900, y=300)  # need to change after adding right pictures.
        self.ok_button.place(x=955, y=350)  # need to change after adding right pictures.
        self.player.inventory.append('part 2')

    def press_ok(self):
        self.ok_button.destroy()
        self.label_info.destroy()
        self.player.locked = False
        self.Back_room_button.destroy()
        SecretRoom(self.master, self.label_im, self.label_text, self.player).prepare_and_start()


class TheEnd:
    def __init__(self, master, label_im, label_text, player):
        self.master = master
        self.label_im = label_im
        self.player = player
        self.ok_button = tkinter.Button(self.master, text='Ok', background='#002238',
                                        foreground='#D6DDE4', width=5, command=lambda: exit())
        label_text.destroy()
        self.player.inventory_button.destroy()
        self.player.hide_button.destroy()

    def prepare_and_start(self):
        self.master.im = ImageTk.PhotoImage(Image.open('the end.jpg'))  # change later
        self.label_im.config(image=self.master.im)
        self.ok_button.place(x=900, y=900)


def text_wrap(new_text):
    wrapped_text = '\n'.join(wrap(new_text, 1270 // len(new_text.split(' '))))
    return wrapped_text


# def show_coordinates(event):
#    x = event.x
#    y = event.y
#    print(x, y)


def make_binds(label_name, leave_im=None, enter_im=None, way=None):
    label_name.config(image=leave_im, cursor='dot')
    if enter_im:
        label_name.bind("<Enter>", lambda event: event.widget.config(image=enter_im))
    if leave_im:
        label_name.bind("<Leave>", lambda event: event.widget.config(image=leave_im))
    if way:
        label_name.bind("<Button-1>", lambda event: way())


class PlayerControl:
    def __init__(self, master, label_text):
        self.master = master
        self.label_text = label_text
        self.label_inventory = tkinter.Label(self.master)
        self.label_key = tkinter.Label(self.master)
        self.label_green_number = tkinter.Label(self.master)
        self.label_eye = tkinter.Label(self.master)
        self.label_part1 = tkinter.Label(self.master)
        self.label_part2 = tkinter.Label(self.master)
        self.label_part3 = tkinter.Label(self.master)
        self.label_blue_number = tkinter.Label(self.master)
        self.inventory = []
        self.inventory_isOpen = False
        self.access_to_secret_room = False
        self.access_to_exit = False
        self.locked = False
        self.console_isOpen = False
        self.hide_text = False
        self.inventory_button = tkinter.Button(self.master, text='Inventory', width=15, background='#330066',
                                               foreground='#D6DDE4', command=self.open_inventory, font='Candra')
        self.hide_button = tkinter.Button(self.master, text='Hide', width=15, background='#330066',
                                          foreground='#D6DDE4', command=self.hide, font='Candra')
        self.inventory_button.place(x=410, y=970)
        self.hide_button.place(x=2, y=685)

    def open_inventory(self):
        if not self.inventory_isOpen and not self.locked:
            self.label_inventory = tkinter.Label(self.master, height=13, width=50, font=("Helvetica", 14),
                                                 background='#807F8E', foreground='#D6DDE4', borderwidth=5,
                                                 relief="groove")
            new_label_inventory = self.label_inventory
            new_label_inventory.place(x=600, y=500)
            self.inventory_isOpen = True
            if 'key' in self.inventory:
                im = ImageTk.PhotoImage(Image.open('key.png'))
                self.label_key = tkinter.Label(self.master, image=im, borderwidth=0)
                self.label_key.image = im
                self.label_key.place(x=620, y=520)
            if 'green number' in self.inventory:
                im = ImageTk.PhotoImage(Image.open('green number.png'))
                self.label_green_number = tkinter.Label(self.master, image=im, borderwidth=0)
                self.label_green_number.image = im
                self.label_green_number.place(x=625, y=600)  # need to change after adding right pictures.
            if 'eye' in self.inventory:
                im = ImageTk.PhotoImage(Image.open('eye.png'))
                self.label_eye = tkinter.Label(self.master, image=im, borderwidth=0)
                self.label_eye.image = im
                self.label_eye.place(x=700, y=520)  # need to change after adding right pictures.
            if 'part 2' in self.inventory:
                im = ImageTk.PhotoImage(Image.open('part 2.png'))
                self.label_part2 = tkinter.Label(self.master, image=im, borderwidth=0)
                self.label_part2.image = im
                self.label_part2.place(x=700, y=520)
            if 'part 1' in self.inventory:
                im = ImageTk.PhotoImage(Image.open('part 1.png'))
                self.label_part1 = tkinter.Label(self.master, image=im, borderwidth=0)
                self.label_part1.image = im
                self.label_part1.place(x=780, y=520)
            if 'part 3' in self.inventory:
                im = ImageTk.PhotoImage(Image.open('part 3.png'))
                self.label_part3 = tkinter.Label(self.master, image=im, borderwidth=0)
                self.label_part3.image = im
                self.label_part3.place(x=860, y=520)
            if 'blue number' in self.inventory:
                im = ImageTk.PhotoImage(Image.open('blue number.png'))
                self.label_blue_number = tkinter.Label(self.master, image=im, borderwidth=0)
                self.label_blue_number.image = im
                self.label_blue_number.place(x=700, y=600)

        else:
            self.label_inventory.place_forget()
            self.label_key.place_forget()
            self.label_green_number.place_forget()
            self.label_eye.place_forget()
            self.label_part1.place_forget()
            self.label_part2.place_forget()
            self.label_part3.place_forget()
            self.label_blue_number.place_forget()
            self.inventory_isOpen = False

    def hide(self):
        if not self.inventory_isOpen:
            if not self.hide_text:
                self.label_text.place_forget()
                self.inventory_button.place_forget()
                self.hide_button.place(x=2, y=950)
                self.hide_button.config(text='Return text')
                self.hide_text = True
            else:
                self.label_text.place(x=2, y=718)
                self.inventory_button.place(x=410, y=970)
                self.hide_button.place(x=2, y=685)
                self.hide_button.config(text='Hide')
                self.hide_text = False


def main():
    window = tkinter.Tk()
    window.enter_im = ImageTk.PhotoImage(Image.open('enter button.png'))
    window.geometry('1920x1080')
    window.bind("<Escape>", lambda event: exit())
    label_image = tkinter.Label(window)
    main_text = tkinter.Label(window, height=13, width=50, justify='left', font=("Candra", 14), background='#001933',
                              foreground='#D6DDE4', borderwidth=5, anchor='nw')
    player = PlayerControl(window, main_text)
    SoggyRoom(window, label_image, main_text, player).prepare_and_start()
    main_text.place(x=2, y=718)
    label_image.pack()
    window.mainloop()


if __name__ == '__main__':
    main()

# coding: utf-8
# license: GPLv3

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.
    **space_objects** — список объектов, которые воздействуют на тело.
    """

    body.Fx = body.Fy = 0
    for obj in space_objects:
        if body == obj:
            dist = ((body.x - obj.x)**2 + (body.y - obj.y)**2)**0.5
            dist_x = obj.x -  body.x
            dist_y = obj.y -  body.y
            force = gravitational_constant * body.m * obj.m / dist ** 2
            body.Fx = force * dist_x / dist
            body.Fy = force * dist_y / dist
'''
            continue  # тело не действует гравитационной силой на само себя!
        r = ((body.x - obj.x)**2 + (body.y - obj.y)**2)**0.5
        body.Fx += 1  # FIXME: нужно вывести формулу...
        body.Fy += 2  # FIXME: нужно вывести формулу...
'''

def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """
    
    ax = body.Fx/body.m
    ay = body.Fy/body.m
    body.Vx += ax * dt
    body.Vy += ay * dt
    body.x += body.Vx * dt  # FIXME: не понимаю как менять...
    body.y += body.Vy * dt
    # FIXME: not done recalculation of y coordinate!


def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.
    **dt** — шаг по времени
    """

    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")

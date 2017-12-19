import sys
sys.path.append("..")
import camera
import mouse
import scene

class EditorCamera():

    def __init__(self):
        self.pan = False
        self.rotate = False
        self.mouse_start = (0,0)
        self.speed = 2
        self.move = False

    def input(self, key):
        # print(key)
        if key == '+':
            camera.fov += 5
        elif key == '-':
            camera.fov -= 5

        if key == 'p':
            camera.orthographic = not camera.orthographic

        if key == 'middle mouse down':
            self.camera_start = camera.position
            self.pan = True
        if key == 'middle mouse up':
            self.pan = False

        if key == 'right mouse down':
            self.camera_start_rotation = scene.editor.camera_pivot.rotation
            self.rotate = True
        if key == 'right mouse up':
            self.rotate = False

        # zooming, don't zoom if hovering an editor panel
        if not mouse.hovered_entity or not mouse.hovered_entity.is_editor:
            if key == 'scroll up' and mouse.left == False:
                # camera.position += camera.forward * self.speed
                camera.z += self.speed
            if key == 'scroll down' and mouse.left == False:
                # camera.position += camera.back * self.speed
                camera.z -= self.speed

                if camera.orthographic:
                    pass
                    # camera.fov += self.speed


        if self.rotate:
            if key == 'd':
                scene.editor.camera_pivot.position += camera.right * self.speed
                # print(camera.right)
            if key == 'a':
                scene.editor.camera_pivot.position += camera.left * self.speed

            if key == 's':
                scene.editor.camera_pivot.position += camera.back * self.speed
            if key == 'w':
                scene.editor.camera_pivot.position += camera.forward * self.speed



            if key == 'e':
                scene.editor.camera_pivot.position += camera.up * self.speed
            if key == 'q':
                 scene.editor.camera_pivot.position += camera.down * self.speed
            #
            # if key == 'r':
            #     camera.rotation_x += 1 #(camera.rotation[0] -1, camera.rotation[1], camera.rotation[2])
            # if key == 'f':
            #     camera.rotation_x -= 1
            # if key == 't':
            #     camera.rotation_y += 1
            # if key == 'g':
            #     camera.rotation_y -= 1
            # if key == 'y':
            #     camera.rotation += (0,0,10)
            # if key == 'h':
            #     camera.rotation_z -= 10

            # print(camera.cam.getPos())


    def update(self, dt):
        if self.pan:
            camera.x = self.camera_start[0] - mouse.delta[0] * self.speed * 2
            camera.y = self.camera_start[1] - mouse.delta[1] * self.speed * 2
            camera.z = self.camera_start[2]

        if self.rotate:
            scene.editor.camera_pivot.rotation = (
                self.camera_start_rotation[0] + mouse.delta[1] * -self.speed * 20,
                self.camera_start_rotation[1] - mouse.delta[0] * -self.speed * 20,
                0
                )
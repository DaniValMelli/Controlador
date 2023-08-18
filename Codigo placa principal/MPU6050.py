from MPU.MPU6050 import MPU6050
import math

i2c_bus = 1
device_address = 0x68
# The offsets are different for each device and should be changed
# accordingly using a calibration procedure
x_accel_offset = -2725
y_accel_offset = -1545
z_accel_offset = 2242
x_gyro_offset = 5
y_gyro_offset = 3
z_gyro_offset = 110
enable_debug_output = True

mpu = MPU6050(i2c_bus, device_address, x_accel_offset, y_accel_offset,
              z_accel_offset, x_gyro_offset, y_gyro_offset, z_gyro_offset,
              enable_debug_output)

mpu.dmp_initialize()
mpu.set_DMP_enabled(True)
mpu_int_status = mpu.get_int_status()
print(hex(mpu_int_status))

packet_size = mpu.DMP_get_FIFO_packet_size()
print(packet_size)
FIFO_count = mpu.get_FIFO_count()
print(FIFO_count)

count = 0
FIFO_buffer = [0]*64

FIFO_count_list = list()

def readMPU():

    try:
        FIFO_count = mpu.get_FIFO_count()
        mpu_int_status = mpu.get_int_status()
    
        while FIFO_count < packet_size:
            FIFO_count = mpu.get_FIFO_count()
        FIFO_buffer = mpu.get_FIFO_bytes(packet_size)
        
        quat = mpu.DMP_get_quaternion_int16(FIFO_buffer)
        grav = mpu.DMP_get_gravity(quat)
        roll_pitch_yaw = mpu.DMP_get_roll_pitch_yaw(quat,grav)
        angulo = roll_pitch_yaw.x
        mpu.reset_FIFO()
    except Exception as e:
        angulo = readMPU()
        
    return math.degrees(angulo)

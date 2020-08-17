import tensorflow as tf
from keras import backend as K

# keras or tensorflowにて，使用GPUメモリ等を設定
def gpuConfig(allow_growth=True,memory_fraction=1.0,gpu_id=0):
    config = tf.ConfigProto(
        gpu_options=tf.GPUOptions(
            per_process_gpu_memory_fraction = memory_fraction,
            visible_device_list=str(gpu_id), # specify GPU number
            allow_growth=allow_growth
        )
    )
    sess = tf.Session(config=config)
    K.set_session(sess)
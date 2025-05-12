# 生成一个txt文件，包含MinIO中指定bucket下的所有jpg文件的URL
# 用于label-studio上传minIO中的图片
from minio import Minio

endpoint = '192.168.1.200:9000'
client = Minio(endpoint,
               access_key='minioadmin',
               secret_key='minioadmin',
               secure=True)  # 这个可能要修改

bucket_name = "tfds"

objects = client.list_objects(bucket_name, prefix='TFDS_单步检测', recursive=True)

with open("./file_list.txt", 'w', encoding='utf-8') as f:
    for obj in objects:
        if obj.object_name.endswith(".jpg"):
            f.write(f"http://{endpoint}/{bucket_name}/{obj.object_name}\n")

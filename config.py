import os

# Directories
this_dir = os.path.dirname(__file__)
data_dir = os.path.join(this_dir, 'data')
photos_dir = os.path.join(data_dir, 'photos')
videos_dir = os.path.join(data_dir, 'videos')

# Cloud Storage settings
seconds_between_upload_retries = 60.0
cloud_storage_name = 'amazon'
cloud_data_dir = cloud_storage_name + ':/lifelog'
cloud_photos_dir = cloud_data_dir
cloud_videos_dir = cloud_data_dir

# Photography settings
seconds_between_photos = 20.0
burst_mode = True

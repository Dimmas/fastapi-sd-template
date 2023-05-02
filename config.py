from dataclasses import dataclass


# AWS Creds
@dataclass
class AWSConfig:
    aws_access_key_id = '****************'
    aws_secret_access_key = '****************'
    bucket_name = 'landscape'
    host_name = 'https://867320.selcdn.ru'


futures = ['flowerbed', 'track', 'lawn', 'herbal', 'retaining walls', 'stone', 'coating', 'furniture', 'sculptures',
           'gazebos', 'reservoirs', 'buildings', 'hedge flower border', 'curbs blind spots', 'stairs', 'bridges',
           'lighting', 'fountains', 'pot or vases or containers', 'stream', 'hearth, bonfire', 'barbecue', 'trees',
           'bushes', 'flowers', 'decking', 'waterfall', 'arches, pergolas', 'flower border', 'green hedge', 'paving']

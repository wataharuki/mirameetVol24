import os
import OperationOject # 操作対象の設定情報取得
from google.cloud import storage

# GCS認証設定
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = OperationOject.GOOGLE_APPLICATION_CREDENTIALS

# GCSクライアント変数宣言
client = storage.Client()

# GCSバケット取得
bucket = client.get_bucket(OperationOject.bucket_name)

# CSVファイルアップロード
blob = bucket.blob(os.path.basename(OperationOject.source_file_name))
blob.upload_from_filename(OperationOject.source_file_name)

print('File {} uploaded to {}.'.format(
    OperationOject.source_file_name,
    bucket))
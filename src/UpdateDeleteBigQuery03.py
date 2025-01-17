import os
import OperationObject # 操作対象の設定情報取得
from google.cloud import bigquery

# GCS認証設定
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = OperationObject.GOOGLE_APPLICATION_CREDENTIALS

client = bigquery.Client()
# 更新SQL生成
updateQuery = "UPDATE `{0}.{1}.{2}` SET mira_text = '更新' WHERE id = 2".\
    format(OperationObject.project_id, OperationObject.dataset_id, OperationObject.table_id)
# SQL実行
updateRows = client.query(updateQuery).result()
print("Updated ID=2.")

# 削除SQL生成
deleteQuery = "DELETE `{0}.{1}.{2}` WHERE id = 3".\
    format(OperationObject.project_id, OperationObject.dataset_id, OperationObject.table_id)
# SQL実行
deleteRows = client.query(deleteQuery).result()

print("deleted ID=3.")


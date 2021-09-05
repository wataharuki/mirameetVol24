# mirameetVol24

**目次**

- 【Chapter1】事前準備内容確認
- 【Chapter2】GCPの設定と確認
- 【Chapter3】各処理の実行

***
## 【Chapter1】事前準備内容確認 
### ⑴GCPアカウントの確認
![image](https://user-images.githubusercontent.com/66664167/131997557-701aad45-03db-4835-9f8e-5496c7027fd9.png)

### ⑵pythonのバージョン確認
```
python -V
```
3系が入っていることを確認
![image](https://user-images.githubusercontent.com/66664167/131998433-b1949745-ba65-46d4-b5c3-2ea2601d42a2.png)

### ⑵Dockerのバージョン確認
```
docker version
```
★★★Docker手順
```
docker-compose up -d --build
```


## 【Chapter2】GCPの設定と確認
### ⑴GCSバケット作成
![image](https://user-images.githubusercontent.com/66664167/132120811-da7a4fbd-3872-4a26-bb26-1f023e9c61c3.png)

![image](https://user-images.githubusercontent.com/66664167/131999368-51c04a79-8add-47f6-9cdc-4bbea8a1ecbb.png)
![image](https://user-images.githubusercontent.com/66664167/131999409-4fa424e4-d705-4e93-9c8d-b28c0e4f6121.png)

↓作成完了
![image](https://user-images.githubusercontent.com/66664167/132121232-2c896ad7-c91e-47f0-8c49-7e0f8f7ecf8d.png)
![image](https://user-images.githubusercontent.com/66664167/131999485-70e142b1-1e12-4bc3-918f-d1bb3491c425.png)

### ⑵GCS内権限設定
![image](https://user-images.githubusercontent.com/66664167/131999600-04438ce6-42c1-4c32-bd83-69c067d49479.png)

### ⑶サービスアカウントの作成と、秘密鍵ファイルの取得・配置
![image](https://user-images.githubusercontent.com/66664167/132000054-5aaa6f86-3fa6-440b-a276-f53054b6e061.png)
#### 1.サービスアカウントの作成
![image](https://user-images.githubusercontent.com/66664167/132000112-824bc2a9-0f79-41d9-8011-8cfec2da1fbc.png)
![image](https://user-images.githubusercontent.com/66664167/132000238-2a7ca620-f0b2-420d-b57b-6c06187cba3e.png)
![image](https://user-images.githubusercontent.com/66664167/132000262-3c2b662d-61b3-40ae-aa68-cc1421f8ac8f.png)
↓作成完了
![image](https://user-images.githubusercontent.com/66664167/132000331-11d9d0de-1aa1-49a3-82fa-25e805c9f9e1.png)

#### 2.秘密鍵の作成
![image](https://user-images.githubusercontent.com/66664167/132000660-9b1497de-b4ad-4fee-ac14-d73b381bd17c.png)
※json形式のキーをダウンロード
![image](https://user-images.githubusercontent.com/66664167/132000704-9514ee5b-4f93-4d2c-bbdc-54fe071adfcf.png)
↓ダウンロード完了
![image](https://user-images.githubusercontent.com/66664167/132000791-964e946b-9917-4ea2-ad16-7a83b05c3c2e.png)

#### 3.秘密鍵の配置
・配置先
```
mirameet_vol24\credential
```
・ファイル名
```
key.json
```

#### 4.BigQueryAPIの有効化
![image](https://user-images.githubusercontent.com/66664167/132012749-301fe76d-fc7e-4c57-81ad-10cc0dd24e5b.png)
![image](https://user-images.githubusercontent.com/66664167/132012713-982127fa-9d43-4d0f-923f-c0227ed42eaa.png)
![image](https://user-images.githubusercontent.com/66664167/132012595-534dec08-5082-4bb6-a5ba-6ae6360c848a.png)

#### 5.データセットの作成
![image](https://user-images.githubusercontent.com/66664167/132002556-7632d683-1946-4804-b894-18119b659b14.png)
↓作成完了
![image](https://user-images.githubusercontent.com/66664167/132002744-cd3b7837-24bb-4c6f-b7e1-a65fe61bb3ab.png)

#### 6.OperationObject.pyの編集
・url_gs_example_csv
![image](https://user-images.githubusercontent.com/66664167/132121160-a0454d09-fe83-4020-bad1-06d7bd7d026f.png)
「gsutil URI」をコピーして置換
（例）
```
url_gs_example_csv="gs://mira-example/gcs-example.csv"
↓
url_gs_example_csv="gs://sechico-mirameet_vol24/gcs-example.csv"
```
・bucket_name
![image](https://user-images.githubusercontent.com/66664167/132121193-57c28457-3e65-404f-be9c-de3b0db28271.png)
「名前」をコピーして置換
（例）
```
bucket_name = "mira-example"
↓
bucket_name = "sechico-mirameet_vol24"
```
・project_id
![image](https://user-images.githubusercontent.com/66664167/132121599-48e7f366-e197-4192-bed0-152372030482.png)
```
「プロジェクトID」をコピーして置換
（例）
project_id = "erudite-pride-323410"
↓
project_id = "sylvan-surf-322711"
```
・dataset_id
![image](https://user-images.githubusercontent.com/66664167/132121662-f16bef70-ad6d-42d8-83a0-e2a9923df4f4.png)
「データセットID」をコピーして置換
（例）
```
bucket_name = "mira_vol24"
↓
bucket_name = "sechico_0905"
```
・table_id

「テーブルID」をコピーして置換
（例）
```
bucket_name = "mira-example"
↓
bucket_name = "sechico-mirameet_vol24"
```

***
## 【Chapter3】各処理の実行

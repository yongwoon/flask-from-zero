# Login

1. login に成功したら、server から session 情報を browser に返す
2. Client は session 情報を cookie と呼ばれる領域に保存
3. 以後、Client はその session 情報を付与して reqeust し、 server はその session 情報を正しいか確認することで、login しているかどうかを判別します。

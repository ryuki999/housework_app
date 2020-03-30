from django.db import models

#CharFieldは255文字のmax_lengthを持ち、 TextFieldは255文字以上を保持できる。
#models.AutoField(primary_key=True):カスタムの主キー
#primary_key=Trueがどこにもなければ自動でidが生成されインクリメントされる

#userクラス:ユーザ情報
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
    #クラスの値を出力する際にここが出力される
    def __str__(self):
        return "output:" + str(self.user_id) + "," + str(self.username) + "," + str(self.password)

#houseworkクラス:家事の種類
class Housework(models.Model):
    housework_id = models.AutoField(primary_key=True)
    housework_name = models.CharField(max_length=100)
    point = models.IntegerField(default=0)

    def __str__(self):
        return "output:" + str(self.housework_id) + "," + str(self.housework_name) + "," + str(self.point)


#work_reportクラス:家事遂行報告
class Workreport(models.Model):
    workreport_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE, \
            related_name="workreport_user_id")
    housework_id = models.ForeignKey(Housework,on_delete=models.CASCADE, \
            related_name="workreport_housework_id")
    rep_date = models.DateField()

    def __str__(self):
        return "output:" + str(self.workreport_id) + "," + str(self.user_id) + "," \
            + str(self.housework_id) + "," + str(self.rep_date)

    class Meta:
        ordering = ("-rep_date",)

#day_rankクラス:日ごとの順位
class Day_rank(models.Model):
    date_id = models.AutoField(primary_key=True)
    date = models.DateField()
    user_id = models.ForeignKey(User,on_delete=models.CASCADE, \
            related_name="day_rank_user_id")
    total_point = models.IntegerField(default=0)

    def __str__(self):
        return "output:" + str(self.date_id) + "," + str(self.date) + "," \
            + str(self.user_id) + "," + str(self.total_point)

    class Meta:
        ordering = ("-date","-total_point")
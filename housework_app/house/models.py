from django.db import models

# CharFieldは255文字のmax_lengthを持ち、 TextFieldは255文字以上を保持できる。
# models.AutoField(primary_key=True):カスタムの主キー
# primary_key=Trueがどこにもなければ自動でidが生成されインクリメントされる


class User(models.Model):
    # userクラス:ユーザ情報
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    # クラスの値を出力する際にここが出力される
    def __str__(self):
        return "output:" + str(self.user_id) + "," + str(self.username) + \
                "," + str(self.password)


class Housework(models.Model):
    # houseworkクラス:家事の種類
    housework_id = models.AutoField(primary_key=True)
    housework_name = models.CharField(max_length=100)
    point = models.IntegerField(default=0)

    def __str__(self):
        return "output:" + str(self.housework_id) + "," + \
                str(self.housework_name) + "," + str(self.point)


class Workreport(models.Model):
    # work_reportクラス:家事遂行報告
    workreport_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name="workreport_user_id")
    housework_id = models.ForeignKey(Housework, on_delete=models.CASCADE,
                                     related_name="workreport_housework_id")
    rep_date = models.DateField()

    def __str__(self):
        return "output:" + str(self.workreport_id) + "," + str(self.user_id) \
         + "," + str(self.housework_id) + "," + str(self.rep_date)

    class Meta:
        ordering = ("-rep_date",)


class Day_rank(models.Model):
    # day_rankクラス:日ごとの順位
    date_id = models.AutoField(primary_key=True)
    date = models.DateField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name="day_rank_user_id")
    total_point = models.IntegerField(default=0)

    def __str__(self):
        return "output:" + str(self.date_id) + "," + str(self.date) + "," \
            + str(self.user_id) + "," + str(self.total_point)

    class Meta:
        ordering = ("-date", "-total_point")

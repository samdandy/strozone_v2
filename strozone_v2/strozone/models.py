from django.db import models

# Create your models here.




class league_table(models.Model):
    league_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    league_img_url = models.CharField(max_length=1000)
    source_system_id = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
          return self.name

class stat_type_table(models.Model):
    stat_type_id = models.AutoField(primary_key=True)
    display_name = models.CharField(max_length=100)
    lookup_name = models.CharField(max_length=100)
    group_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
          return self.lookup_name

class division_table(models.Model):
    division_id = models.AutoField(primary_key=True)
    league =models.ForeignKey(league_table, on_delete=models.CASCADE) 
    name = models.CharField(max_length=100)
    source_system_id = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
          return self.name

class team_table(models.Model):
    team_id = models.AutoField(primary_key=True)
    division = models.ForeignKey(division_table, on_delete=models.CASCADE) 
    name = models.CharField(max_length=100)
    city_name = models.CharField(max_length=100)
    team_img_url = models.CharField(max_length=1000)
    source_system_id = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
          return self.name

class injured_list_table(models.Model):
    injured_list_id = models.AutoField(primary_key=True)
    team = models.ForeignKey(team_table, on_delete=models.CASCADE)
    player_name = models.CharField(max_length=500)
    position = models.CharField(max_length=50)
    updated = models.DateTimeField()
    injury_body_part = models.CharField(max_length=100)
    injury_description = models.CharField(max_length=1000)
    crc_id = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
          return self.injured_list_id

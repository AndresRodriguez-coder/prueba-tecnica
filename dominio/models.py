from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Plot ( models.Model):
    name = models.CharField()
    SABANA_CHOICES= (
        ('SUBACHOQUE', 'Subachoque'),
        ('ROSAL', 'Subachoque'),
        ('FACATATIVA', 'Subachoque'),
        ('MADRID', 'Madrid'),
        ('ZIPACON', 'Zipacon'),
        ('BOJACA', 'Bojaca'),
        ('MOSQUERA', 'Mosquera'),
        ('FUNZA', 'Funza'),
        ('COTA', 'Cota'),
        ('TENJO', 'Tenjo'),
        
        
    )
    municipality = models.TextField ( choices=SABANA_CHOICES , default='MOSQUERA')
    crop_type = models.CharField(max_length=50)
    area = models.FloatField()
    
    def __str__(self):
        return self.name


    
class FieldActivity(models.Model):
    plot_id = models.ForeignKey(Plot, on_delete=models.CASCADE)
    activity_type= models.CharField()
    performed_at = models.DateField(auto_now_add=True)
    notes = models.TextField( null=True)
    


class HarvestBatch (models.Model):
    plot_id = models.ForeignKey(Plot, on_delete=models.CASCADE)
    harvest_date = models.DateField()
    quantity_kg = models.FloatField()
    quality_grade = models.CharField()
    moisture_pct = models.IntegerField()
    ph_soil = models.IntegerField(validators=[MaxValueValidator(14)])
    


class OutboundOrder (models.Model):
    harvest_id = models.ForeignKey(HarvestBatch, on_delete=models.CASCADE)
    client_name = models.CharField()
    destination_city = models.CharField()
    dispatched_at = models.DateField( auto_now_add=True)
    quantity_kg = models.FloatField(validators=[MaxValueValidator(HarvestBatch.quantity_kg)])
    notes = models.TextField( null=True)

    

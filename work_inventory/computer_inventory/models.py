from django.db import models


# Create your models here.


class Computer(models.Model):
    WINDOWS_TEN = 'WIN10'
    WINDOWS_SEVEN = 'WIN7'
    WINDOWS_TYPE = (
        (WINDOWS_TEN, 'WINDOWS 10'),
        (WINDOWS_SEVEN, 'WINDOWS 7')
    )
    MARKET = '1500 MARKET ST'
    SPE_ONE = 'SPE1'
    SPE_FOURTEEN = 'SPE14'
    SPE_TEN = 'SPE10'
    SILVER_FOUR = 'SILVER 4'
    SILVER_SIX = 'SILVER 6'
    SMILLOW = 'SMILLOW'
    WHITE_SIX = 'WHITE 6'
    PCAM_THREE = 'PCAM3'
    PCAM_FOUR = 'PCAM4'
    GATES_FIVE = 'GATES5'
    GROUND_FOUNDERS_13 = 'GROUND FOUNDERS 013'
    GROUND_FOUNDERS_079 = 'GROUN'
    STEMMLER_HALL = 'STEMMLER HALL'
    RAV_COURTYARD = 'RAV 5 COURTYARD'
    DULLES_TWO = 'DULLES 2'
    DULLES_TWO_COURTYARD = "DULLES 2 COURT"
    SILVER_FIVE = 'SILVER5'
    PRESBY = 'PRESBY'
    MALONEY_FIVE = 'MALONEY 5'
    MALONEY_FOUR = 'MALONEY 4'
    OTHER = "OTHER"

    LOCATION_TYPE = (
        (SILVER_FOUR, 'SILVER 4'),
        (SILVER_FIVE, 'SILVER 5'),
        (SILVER_SIX, "SILVER 6"),
        (WHITE_SIX, "WHITE 6"),
        (PRESBY, 'PRESBY'),
        (PCAM_THREE, 'PCAM3'),
        (PCAM_FOUR, 'PCAM4'),
        (GATES_FIVE, 'GATES 5'),
        (GROUND_FOUNDERS_13, 'GROUND FOUNDERS 013'),
        (GROUND_FOUNDERS_079, 'GROUND FOUNDER 079'),
        (STEMMLER_HALL, 'STEMMLER HALL'),
        (RAV_COURTYARD, 'RAV 5 COURTYARD'),
        (DULLES_TWO, 'DULLES 2'),
        (DULLES_TWO_COURTYARD, "DULLES 2 COURT"),
        (SILVER_FIVE, 'SILVER5'),
        (MARKET, '1500 MARKET ST'),
        (SPE_ONE, 'SPE1'),
        (SPE_FOURTEEN, 'SPE14'),
        (SPE_TEN, 'SPE10'),
        (MALONEY_FIVE, 'MALONEY 5'),
        (MALONEY_FOUR, 'MALONEY 4'),
        (OTHER, 'OTHER')
    )
    T400 = 'T400'
    T410 = 'T410'
    T420 = 'T420'
    T440 = "T440"
    T460 = 'T460'
    T470 = "T470"
    T480 = 'T480'
    T490 = "T490"
    T14S = "T14S"
    P10AE = '10AF'
    P10AF = '10AE'
    P10NS = "10NS"
    P10F5 = '10F5'
    P10S6 = '10S6'
    P10S7 = '10S7'
    P3318 = '3318'
    P3391 = "3391"
    CARBON = 'CARBON'
    P10ML = '10ML'
    P5205 = '5205'
    X1_YOGA = 'X1 YOGA'
    P0870 = "0870"

    MINI = 'MINI'
    SURFACE_LAPTOP = "SURFACE LAPTOP"
    MODEL_OTHER = "OTHER"
    MODEL_TYPES = (
        (T410, 'T410'),
        (T420, 'T420'),
        (T440, 'T440'),
        (T460, 'T460'),
        (T470, 'T470'),
        (T480, 'T480'),
        (T490, 'T490'),
        (CARBON, 'CARBON'),
        (SURFACE_LAPTOP, "SURFACE LAPTOP")
        ,
        (T14S, "T14S"),
        (P10AE, '10AF'),
        (P10AF, '10AE'),
        (P10NS, "10NS"),
        (P10F5, '10F5'),
        (P10S6, '10S6'),
        (P10S7, '10S7'),
        (P3318, '3318'),
        (P3391, "3391"),

        (P10ML, '10ML'),
        (P5205, '5205'),

        (P0870, "0870"),

        (MINI, 'MINI'),

        (MODEL_OTHER, "OTHER"),

    )

    operating_system = models.CharField(max_length=5, choices=WINDOWS_TYPE, default=WINDOWS_TEN)
    computer_name = models.CharField(max_length=7, blank=False, null=True)
    serial_number = models.CharField(max_length=7, blank=False, null=True)
    user_name = models.CharField(max_length=30, blank=False, null=True)
    person_full_name = models.CharField(max_length=40, blank=False, null=True)
    time_stamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    model_number = models.CharField(max_length=14, choices=MODEL_TYPES, blank=False, null=True)
    location = models.CharField(max_length=19, choices=LOCATION_TYPE, null=True)
    comments = models.CharField(max_length=30, blank=True, null=True)
    export_to_CSV = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.computer_name} {self.location}'

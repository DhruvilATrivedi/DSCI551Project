from django import forms

Words =(('0', 'Grammys 2021'),
 ('1', 'Drew Brees'),
 ('2', 'Megan Thee Stallion'),
 ('3', 'Dua Lipa'),
 ('4', 'BTS'),
 ('5', 'Justin Thomas'),
 ('6', 'Doja Cat'),
 ('7', "Zack Snyder's Justice League"),
 ('8', 'Ides of March'),
 ('9', 'Oscar Nominations 2021'),
 ('10', 'Bruno Mars'),
 ('11', 'Marvin Hagler'),
 ('12', 'Kirk Franklin'),
 ('13', 'Billie Eilish'),
 ('14', 'Warriors'),
 ('15', 'Juventus'),
 ('16', 'Helen Storey'),
 ('17', 'Bad Bunny'),
 ('18', 'Blaze Pizza'),
 ('19', 'CBS Sports'),
 ('20', 'Miranda Lambert'),
 ('21', 'Brittany Howard'),
 ('22', 'Maren Morris'),
 ('23', 'Time'),
 ('24', 'Jennifer Lopez'),
 ('25', '#MondayMotivation'),
 ('26', 'Beyoncé'),
 ('27', 'Catholic Church'),
 ('28', '#GRAMMYs'),
 ('29', 'Megan'),
 ('30', 'Woody Allen'),
 ('31', 'Lil Baby'),
 ('32', 'Patriots'),
 ('33', 'Vatican'),
 ('34', 'Doja'),
 ('35', 'Mank'),
 ('36', 'Chivas'),
 ('37', 'Corey Davis'),
 ('38', '#OscarNoms'),
 ('39', 'namjoon'),
 ('40', 'Sound of Metal'),
 ('41', '#mondaythoughts'),
 ('42', 'Julius Caesar'),
 ('43', 'Silk Sonic'),
 ('44', 'AOTY'),
 ('45', 'Best Picture'),
 ('46', 'Gen X'),
 ('47', 'John Oliver'),
 ('48', 'Pats'),
 ('49', 'Lakeith'))


class Key_word_Form(forms.Form):
    key_word = forms.ChoiceField(choices = Words)
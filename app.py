from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# بيانات المشروبات مع الحلويات المقترحة
DEFAULT_DRINKS = [
    # مزاج: سعيد
    {"mood": "سعيد", "drink_name": "موهيتو ماندولين", "description": "غني بالفيتامينات، منعش", "dessert": "تشيز كيك ماندولين", "dessert_desc": "خفيف وحامض يعزز الانتعاش"},
    {"mood": "سعيد", "drink_name": "سبانش لاتيه", "description": "ناعم ولذيذ", "dessert": "بان كيك ماندولين", "dessert_desc": "خفيف وممتع مع السيروب"},
    {"mood": "سعيد", "drink_name": "موهيتو توت أسود", "description": "حيوي ومليء بالنكهة", "dessert": "ميني كوكيز", "dessert_desc": "مقرمش ومبهج"},

    # مزاج: زعلان
    {"mood": "زعلان", "drink_name": "قهوة تركية", "description": "دافئة ومهدئة", "dessert": "بودنق التمر", "dessert_desc": "غني وحلو لتحسين المزاج"},
    {"mood": "زعلان", "drink_name": "لاتيه زعفران", "description": "فاخر ومريح", "dessert": "تيراميسو", "dessert_desc": "كريمي يرفع المعنويات"},
    {"mood": "زعلان", "drink_name": "شاي كركديه", "description": "يهدئ الأعصاب", "dessert": "تشيز مقلوب", "dessert_desc": "ناعم ومرضي"},

    # مزاج: مزاج سيئ
    {"mood": "مزاج سيئ", "drink_name": "شاي كركديه", "description": "يهدئ الأعصاب", "dessert": "ميني كوكيز", "dessert_desc": "بسيط ومريح"},
    {"mood": "مزاج سيئ", "drink_name": "كركدية آيس تي", "description": "منعش وخفيف", "dessert": "تشيز القشد", "dessert_desc": "ناعم ومهدئ"},
    {"mood": "مزاج سيئ", "drink_name": "شاي أخضر", "description": "مهدئ بفضل الثيانين", "dessert": "بودنق شوكلاتة", "dessert_desc": "حلو ومريح"},

    # مزاج: تعبان
    {"mood": "تعبان", "drink_name": "آيس لاتيه", "description": "منعش ويعطي طاقة", "dessert": "براونيز بيكان", "dessert_desc": "غني بالطاقة"},
    {"mood": "تعبان", "drink_name": "آيس أمريكانو", "description": "قوي ومنشط", "dessert": "كوكيز ماندولين", "dessert_desc": "مقرمش وسريع"},
    {"mood": "تعبان", "drink_name": "إسبريسو", "description": "يزيد التركيز", "dessert": "صاج كوكيز", "dessert_desc": "مغذي ومشبع"},

    # مزاج: متوتر
    {"mood": "متوتر", "drink_name": "شاي أخضر", "description": "مهدئ بفضل الثيانين", "dessert": "تشيز القشد", "dessert_desc": "ناعم وخفيف"},
    {"mood": "متوتر", "drink_name": "لاتيه زعفران", "description": "فاخر ومريح", "dessert": "سان سباستيان", "dessert_desc": "كريمي ومهدئ"},
    {"mood": "متوتر", "drink_name": "كركدية", "description": "يخفض التوتر", "dessert": "فرنش توست", "dessert_desc": "دافئ ومريح"},

    # مزاج: مبسوط
    {"mood": "مبسوط", "drink_name": "سبانش لاتيه بستاشيو", "description": "نكهات لذيذة", "dessert": "تيراميسو", "dessert_desc": "كريمي ومميز"},
    {"mood": "مبسوط", "drink_name": "موهيتو ليمون", "description": "منعش وحمضي", "dessert": "كيكة ماندولين", "dessert_desc": "خفيفة ومبهجة"},
    {"mood": "مبسوط", "drink_name": "بستاشيو لاتيه", "description": "غني وممتع", "dessert": "اسبيشل تيراميسو", "dessert_desc": "فاخر ولذيذ"},

    # مزاج: مستعد للعمل
    {"mood": "مستعد للعمل", "drink_name": "إسبريسو", "description": "يزيد التركيز", "dessert": "كوكيز ماندولين", "dessert_desc": "سريع ومقرمش"},
    {"mood": "مستعد للعمل", "drink_name": "V60", "description": "قهوة نقية ومركزة", "dessert": "براونيز بيكان", "dessert_desc": "غني ومنشط"},
    {"mood": "مستعد للعمل", "drink_name": "الفريدو إسبريسو", "description": "قوي وكريمي", "dessert": "صاج كوكيز", "dessert_desc": "مغذي وسريع"},

    # مزاج: هادئ
    {"mood": "هادئ", "drink_name": "لاتيه زعفران", "description": "مهدئ وفاخر", "dessert": "سان سباستيان", "dessert_desc": "كريمي ومريح"},
    {"mood": "هادئ", "drink_name": "كيمكس حار", "description": "نكهة غنية وهادئة", "dessert": "فرنش توست كنافة", "dessert_desc": "دافئ ومميز"},
    {"mood": "هادئ", "drink_name": "موهيتو زعفران", "description": "منعش ومهدئ", "dessert": "تشيز مقلوب", "dessert_desc": "ناعم وهادئ"},

    # مزاج: عطشان
    {"mood": "عطشان", "drink_name": "موهيتو توت بري", "description": "منعش وحيوي", "dessert": "بان كيك ماندولين", "dessert_desc": "خفيف وممتع"},
    {"mood": "عطشان", "drink_name": "موهيتو خوخ", "description": "عصيري ولذيذ", "dessert": "تشيز كيك ماندولين", "dessert_desc": "منعش وحامض"},
    {"mood": "عطشان", "drink_name": "Ice V60", "description": "قهوة باردة منعشة", "dessert": "ميني كوكيز", "dessert_desc": "خفيف ومقرمش"},

   
    
    {"mood": "العائلة", "drink_name": "موهيتو ليمون", "description": "منعش ومحبوب من الجميع", "dessert": "بان كيك ماندولين", "dessert_desc": "خفيف وممتع للكبار والصغار"},
    {"mood": "العائلة", "drink_name": "سبانش لاتيه", "description": "ناعم وكريمي، مثالي للتجمعات", "dessert": "كوكيز ماندولين", "dessert_desc": "مقرمش وسهل المشاركة"},
    {"mood": "العائلة", "drink_name": "آيس لاتيه", "description": "بارد ومنعش، يناسب جميع الأعمار", "dessert": "تشيز كيك ماندولين", "dessert_desc": "حلوى عائلية كلاسيكية"},
    {"mood": "العائلة", "drink_name": "موهيتو توت بري", "description": "ملون وممتع للأطفال والكبار", "dessert": "ميني كوكيز", "dessert_desc": "خفيف ومبهج"},
    {"mood": "العائلة", "drink_name": "بستاشيو لاتيه", "description": "غني ومميز، يضيف لمسة فاخرة", "dessert": "تيراميسو", "dessert_desc": "كريمي ومحبوب من الجميع"},
    {"mood": "العائلة", "drink_name": "كركدية آيس تي", "description": "بارد وملون يجذب الأطفال", "dessert": "براونيز بيكان", "dessert_desc": "غني ومشبع للجميع"},
    {"mood": "العائلة", "drink_name": "إسبريسو", "description": "قوي ومركز لعشاق القهوة", "dessert": "صاج كوكيز", "dessert_desc": "مقرمش ومثالي مع القهوة"},
    {"mood": "العائلة", "drink_name": "V60", "description": "قهوة نقية وخفيفة للجميع", "dessert": "بودنق التمر", "dessert_desc": "حلو ودافئ يناسب التجمعات"},
    {"mood": "العائلة", "drink_name": "قهوة تركية", "description": "تقليدية ودافئة للعائلة", "dessert": "فرنش توست", "dessert_desc": "غني ومريح للجميع"}
]

    


@app.route('/')
def home():
    moods = sorted(set(drink['mood'] for drink in DEFAULT_DRINKS))
    return render_template('index.html', moods=moods)

@app.route('/suggest', methods=['POST'])
def suggest():
    mood = request.form.get('mood')
    drinks = [drink for drink in DEFAULT_DRINKS if drink['mood'] == mood]
    return render_template('result.html', mood=mood, drinks=drinks)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
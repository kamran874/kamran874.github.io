"""Builds the Urdu GTA 6 guide site into ../site.
Set DOMAIN below (or edit sitemap.xml later) before uploading."""
import os, shutil, datetime

DOMAIN = "https://kamran874.github.io"
SITE = "GTA 6 اردو گائیڈ"
OUT = os.path.join(os.path.dirname(__file__), "..")
TODAY = "18 نومبر 2026"
ISO = datetime.date(2026, 11, 18).isoformat()

NAV = [
    ("index.html", "ہوم"),
    ("release-time.html", "ریلیز ٹائم"),
    ("characters.html", "کردار"),
    ("map.html", "نقشہ"),
    ("editions.html", "قیمت و ایڈیشن"),
    ("tracker.html", "پروگریس ٹریکر"),
    ("faq.html", "سوال و جواب"),
]

AD = '<div class="ad"><!-- AdSense ad unit goes here --><span class="en">Ad</span></div>'

def page(fname, title, desc, body, extra_js=""):
    nav = "".join(
        f'<a href="{h}"{" class=active" if h == fname else ""}>{t}</a>' for h, t in NAV
    )
    return f"""<!DOCTYPE html>
<html lang="ur" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | {SITE}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{DOMAIN}/{'' if fname == 'index.html' else fname}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:locale" content="ur_PK">
<link rel="stylesheet" href="style.css">
<!-- ADSENSE: paste your AdSense <script> tag here after approval -->
</head>
<body>
<header><div class="bar">
<a class="logo" href="index.html"><span class="en">GTA 6</span> اردو گائیڈ</a>
<nav>{nav}</nav>
</div></header>
<main>
{body}
</main>
<footer>
<p>یہ ایک غیر سرکاری فین ویب سائٹ ہے۔ ہمارا <span class="en">Rockstar Games</span> یا <span class="en">Take-Two</span> سے کوئی تعلق نہیں۔ <span class="en">Grand Theft Auto</span> ان کا ٹریڈ مارک ہے۔</p>
<p><a href="about.html">ہمارے بارے میں</a><a href="privacy.html">پرائیویسی پالیسی</a><a href="contact.html">رابطہ</a></p>
<p class="en">© 2026 GTA 6 Urdu Guide</p>
</footer>
{extra_js}
</body>
</html>"""

E = lambda s: f'<span class="en">{s}</span>'

PAGES = {}

# ---------------- HOME ----------------
PAGES["index.html"] = ("GTA 6 اردو میں — ریلیز، کردار، نقشہ اور گائیڈز",
"جی ٹی اے 6 کی مکمل معلومات اردو میں: پاکستان میں ریلیز ٹائم، قیمت، کردار، لیونیڈا کا نقشہ اور پروگریس ٹریکر۔",
f"""
<h1>{E('GTA 6')} — سب کچھ اردو میں</h1>
<p class="lead">{E('Grand Theft Auto VI')} آخرکار آ رہا ہے۔ یہاں آپ کو ریلیز ٹائم، قیمت، کردار، نقشہ اور گیم کی گائیڈز آسان اردو میں ملیں گی۔</p>
<p class="updated">آخری اپڈیٹ: {TODAY}</p>

<div class="card">
<h3>فوری معلومات</h3>
<table>
<tr><th>ریلیز کی تاریخ</th><td>جمعرات، 19 نومبر 2026</td></tr>
<tr><th>پلیٹ فارم</th><td>{E('PS5 / PS5 Pro')} اور {E('Xbox Series X|S')}</td></tr>
<tr><th>{E('PC')} ورژن</th><td>ابھی اعلان نہیں ہوا</td></tr>
<tr><th>ان لاک ٹائم</th><td>ہر ریجن میں مقامی وقت کے مطابق رات 12 بجے</td></tr>
<tr><th>قیمت ({E('US')})</th><td>اسٹینڈرڈ {E('$79.99')} — الٹیمیٹ {E('$99.99')}</td></tr>
<tr><th>ڈاؤن لوڈ سائز</th><td>تقریباً {E('210 GB')}</td></tr>
<tr><th>کہانی کہاں ہے؟</th><td>لیونیڈا ریاست اور وائس سٹی</td></tr>
</table>
</div>
{AD}
<h2>گائیڈز</h2>
<div class="grid">
<a class="card link" href="release-time.html"><h3>پاکستان میں کب کھلے گا؟</h3><p>اپنے اکاؤنٹ کا ریجن چنیں اور پاکستانی وقت میں ان لاک ٹائم اور کاؤنٹ ڈاؤن دیکھیں۔</p></a>
<a class="card link" href="characters.html"><h3>تمام کردار</h3><p>جیسن، لوسیا اور باقی تمام تصدیق شدہ کردار — کون کون ہے؟</p></a>
<a class="card link" href="map.html"><h3>لیونیڈا کا نقشہ</h3><p>چھ ریجنز: وائس سٹی سے ماؤنٹ کالاگا تک۔</p></a>
<a class="card link" href="editions.html"><h3>کون سا ایڈیشن خریدیں؟</h3><p>اسٹینڈرڈ اور الٹیمیٹ کی قیمت اور فرق۔</p></a>
<a class="card link" href="tracker.html"><h3>پروگریس ٹریکر</h3><p>اپنی گیم کی پیش رفت ٹک کریں — آپ کے فون میں محفوظ رہتی ہے۔</p></a>
<a class="card link" href="faq.html"><h3>سوال و جواب</h3><p>{E('PS4')}؟ {E('PC')}؟ {E('GTA Online')}؟ عام سوالوں کے جواب۔</p></a>
</div>
{AD}
""")

# ---------------- RELEASE TIME ----------------
RT_JS = """<script>
(function(){
  var R = {
    ae:{n:'متحدہ عرب امارات (UAE) اکاؤنٹ', t:'2026-11-18T20:00:00Z'},
    sa:{n:'سعودی عرب اکاؤنٹ', t:'2026-11-18T21:00:00Z'},
    pk:{n:'پاکستان کا مقامی وقت', t:'2026-11-18T19:00:00Z'},
    in:{n:'انڈیا اکاؤنٹ', t:'2026-11-18T18:30:00Z'},
    uk:{n:'برطانیہ (UK) اکاؤنٹ', t:'2026-11-19T00:00:00Z'},
    us:{n:'امریکہ / کینیڈا اکاؤنٹ (PS5)', t:'2026-11-19T05:00:00Z'}
  };
  var sel = document.getElementById('region'), out = document.getElementById('pkt'),
      cd = document.getElementById('cd'), mine = document.getElementById('mine'), timer;
  function fmt(d, tz){
    try { return d.toLocaleString('en-GB',{timeZone:tz, weekday:'short', day:'numeric', month:'short', hour:'numeric', minute:'2-digit', hour12:true}); }
    catch(e){ return d.toUTCString(); }
  }
  function pad(n){ return (n<10?'0':'')+n; }
  function show(){
    var r = R[sel.value], d = new Date(r.t);
    out.textContent = fmt(d,'Asia/Karachi');
    var tz; try { tz = Intl.DateTimeFormat().resolvedOptions().timeZone; } catch(e){}
    mine.textContent = tz && tz !== 'Asia/Karachi' ? ('آپ کے فون کے وقت کے مطابق: ' + fmt(d, tz)) : '';
    clearInterval(timer);
    function tick(){
      var s = Math.floor((d - new Date())/1000);
      if (s <= 0){ cd.textContent = 'ان لاک ہو چکا ✔'; clearInterval(timer); return; }
      var h = Math.floor(s/3600), m = Math.floor(s%3600/60), x = s%60;
      cd.textContent = (h>=24 ? Math.floor(h/24)+'d ' + pad(h%24) : pad(h)) + ':' + pad(m) + ':' + pad(x);
    }
    tick(); timer = setInterval(tick, 1000);
  }
  for (var k in R){ var o = document.createElement('option'); o.value=k; o.textContent=R[k].n; sel.appendChild(o); }
  sel.value = 'ae'; sel.addEventListener('change', show); show();
})();
</script>"""

PAGES["release-time.html"] = ("GTA 6 پاکستان میں کب ریلیز ہوگا؟ ان لاک ٹائم اور کاؤنٹ ڈاؤن",
"جی ٹی اے 6 پاکستان میں کس وقت کھلے گا؟ اپنا پلے اسٹیشن یا ایکس باکس اکاؤنٹ ریجن چنیں اور پاکستانی وقت میں ان لاک ٹائم دیکھیں۔",
f"""
<h1>{E('GTA 6')} پاکستان میں کب کھلے گا؟</h1>
<p class="lead">{E('GTA 6')} ایک ساتھ پوری دنیا میں نہیں کھلتا۔ ہر ریجن میں یہ <b>مقامی وقت کے مطابق 19 نومبر کی رات 12 بجے</b> ان لاک ہوتا ہے۔ سب سے پہلے نیوزی لینڈ میں کھلتا ہے، پھر وقت کے ساتھ مغرب کی طرف۔</p>
<p class="updated">آخری اپڈیٹ: {TODAY}</p>

<div class="card">
<h3>اپنا اکاؤنٹ ریجن چنیں</h3>
<p>زیادہ تر پاکستانی گیمرز {E('UAE')}، سعودی، {E('UK')} یا {E('US')} اکاؤنٹ استعمال کرتے ہیں۔ گیم اکثر <b>اکاؤنٹ کے ریجن</b> کے حساب سے کھلتی ہے۔</p>
<p><select id="region" aria-label="ریجن"></select></p>
<p>پاکستانی وقت میں ان لاک:</p>
<p class="big en" id="pkt">—</p>
<p class="updated" id="mine"></p>
<p>باقی وقت:</p>
<p class="count" id="cd">—</p>
</div>

<div class="note">یہ اوقات اسٹور کے "مقامی رات 12 بجے" والے اصول سے نکالے گئے ہیں۔ اصل وقت کے لیے اپنے {E('PlayStation Store')} یا {E('Microsoft Store')} پر گیم کا پیج ضرور چیک کریں۔ {E('Xbox')} پر وقت تھوڑا مختلف ہو سکتا ہے۔</div>
{AD}
<h2>ریجن کے حساب سے ٹیبل (پاکستانی وقت)</h2>
<table>
<tr><th>اکاؤنٹ ریجن</th><th>پاکستان میں ان لاک</th></tr>
<tr><td>انڈیا</td><td>18 نومبر، رات 11:30</td></tr>
<tr><td>پاکستان کا مقامی وقت</td><td>19 نومبر، رات 12:00</td></tr>
<tr><td>{E('UAE')}</td><td>19 نومبر، رات 1:00</td></tr>
<tr><td>سعودی عرب</td><td>19 نومبر، رات 2:00</td></tr>
<tr><td>{E('UK')}</td><td>19 نومبر، صبح 5:00</td></tr>
<tr><td>{E('US')} / کینیڈا ({E('PS5')})</td><td>19 نومبر، صبح 10:00</td></tr>
</table>

<h2>ان لاک سے پہلے یہ کر لیں</h2>
<ul>
<li>گیم پہلے سے پری لوڈ کر لیں — سائز تقریباً {E('210 GB')} ہے، پاکستانی انٹرنیٹ پر کئی گھنٹے لگ سکتے ہیں۔</li>
<li>کنسول کا سسٹم اپڈیٹ چیک کریں۔</li>
<li>کنسول کو "ریسٹ موڈ" میں انٹرنیٹ سے جڑا رہنے دیں تاکہ ڈے ون پیچ خود ڈاؤن لوڈ ہو جائے۔</li>
<li>اگر لوڈ شیڈنگ کا مسئلہ ہے تو {E('UPS')} پر کنسول اور راؤٹر چلائیں۔</li>
</ul>
<p>مکمل لسٹ کے لیے <a href="tracker.html">پروگریس ٹریکر</a> دیکھیں۔</p>
{AD}
""", RT_JS)

# ---------------- CHARACTERS ----------------
chars = [
 ("لوسیا کامینوس", "Lucia Caminos", "مرکزی کردار (کھیلنے کے قابل)",
  "مین لائن {gta} سیریز کی پہلی خاتون مرکزی کردار۔ مشکل زندگی گزاری، جیل بھی کاٹی، اور اب باہر آ کر بہتر زندگی کے لیے بڑے منصوبے بنا رہی ہے۔"),
 ("جیسن ڈووال", "Jason Duval", "مرکزی کردار (کھیلنے کے قابل)",
  "سابق فوجی جو لیونیڈا کیز میں غلط دھندوں میں پھنس گیا۔ لوسیا کا ساتھی — دونوں کی کہانی ایک ساتھ چلتی ہے۔"),
 ("کیل ہیمپٹن", "Cal Hampton", "جیسن کا دوست",
  "شکی مزاج مگر ذہین۔ زیادہ وقت گھر پر گزارتا ہے، کوسٹ گارڈ کی ریڈیو بات چیت سنتا ہے اور ہر چیز میں سازش ڈھونڈتا ہے۔"),
 ("برائن ہیڈر", "Brian Heder", "جیسن کا باس",
  "لیونیڈا کیز کا پرانا کھلاڑی جس کے لیے جیسن کام کرتا ہے۔"),
 ("بوبی آئیک", "Boobie Ike", "وائس سٹی کا لوکل بزنس مین",
  "وائس سٹی کی مشہور شخصیت جو کئی کاروبار چلاتا ہے اور شہر کی گلیوں کو اچھی طرح جانتا ہے۔"),
 ("ڈری کوان پریسٹ", "Dre'Quan Priest", "میوزک بزنس",
  "بوبی آئیک کے ساتھ میوزک کے کاروبار سے جڑا ہوا، نئے فنکاروں کو آگے لانا چاہتا ہے۔"),
 ("ریئل ڈائمز", "Real Dimez (Bae-Luxe & Roxy)", "ریپ جوڑی",
  "دو دوستوں کی ریپ جوڑی جو سوشل میڈیا اور میوزک کے ذریعے مشہور ہونا چاہتی ہیں۔"),
 ("راؤل بوتیستا", "Raul Bautista", "تجربہ کار بینک ڈاکو",
  "پرانا اور بے خوف بینک ڈاکو جو ہر واردات میں حد سے آگے جانے کو تیار رہتا ہے۔"),
]
cards = "".join(
    f'<div class="card"><h3>{u}</h3><p class="en" style="color:var(--muted)">{en}</p><span class="tag">{role}</span><p>{d.format(gta=E("GTA"))}</p></div>'
    for u, en, role, d in chars)
PAGES["characters.html"] = ("GTA 6 کے تمام کردار — جیسن، لوسیا اور باقی",
"جی ٹی اے 6 کے تمام تصدیق شدہ کردار اردو میں: لوسیا کامینوس، جیسن ڈووال، کیل، بوبی آئیک، راؤل اور دیگر۔",
f"""
<h1>{E('GTA 6')} کے تمام کردار</h1>
<p class="lead">{E('GTA 6')} میں دو کھیلنے کے قابل مرکزی کردار ہیں — جیسن اور لوسیا، جو آپس میں ایک جوڑا ہیں۔ نیچے وہ کردار ہیں جن کی {E('Rockstar')} نے تصدیق کی ہے۔</p>
<p class="updated">آخری اپڈیٹ: {TODAY} — گیم آنے کے بعد مزید کردار شامل کیے جائیں گے۔</p>
{AD}
<div class="grid">{cards}</div>
{AD}
""")

# ---------------- MAP ----------------
regions = [
 ("وائس سٹی", "Vice City", "میامی سے متاثر",
  "لیونیڈا کا سب سے بڑا شہر اور کہانی کا مرکز۔ ساحل، نائٹ لائف، اونچی عمارتیں اور تیز رفتار شہری زندگی۔"),
 ("لیونیڈا کیز", "Leonida Keys", "فلوریڈا کیز سے متاثر",
  "جنوب کے چھوٹے جزیرے جو پلوں سے جڑے ہیں۔ کشتیاں، مچھلیاں، اور جیسن کی کہانی کا آغاز یہیں سے۔"),
 ("گراس ریورز", "Grassrivers", "ایورگلیڈز سے متاثر",
  "دلدلی علاقہ، گھاس کے میدان اور مگرمچھ۔ ایئر بوٹ اور جنگلی حیات کے لیے مشہور۔"),
 ("پورٹ گیلہورن", "Port Gellhorn", "فلوریڈا پین ہینڈل سے متاثر",
  "ایک پرانا صنعتی بندرگاہی قصبہ جس کے اچھے دن گزر چکے ہیں۔"),
 ("ایمبروزیا", "Ambrosia", "دیہی فلوریڈا سے متاثر",
  "دیہی اور صنعتی علاقہ — کھیت، فیکٹریاں اور چھوٹے قصبے۔"),
 ("ماؤنٹ کالاگا نیشنل پارک", "Mount Kalaga National Park", "شمالی سرحد",
  "جنگلات، پہاڑی راستے اور دریا — آف روڈ اور شکار جیسی سرگرمیوں کا علاقہ۔"),
]
rc = "".join(
    f'<div class="card"><h3>{u}</h3><p class="en" style="color:var(--muted)">{en}</p><span class="tag">{tag}</span><p>{d}</p></div>'
    for u, en, tag, d in regions)
PAGES["map.html"] = ("GTA 6 کا نقشہ — لیونیڈا کے 6 ریجنز اردو میں",
"جی ٹی اے 6 کا نقشہ: لیونیڈا ریاست کے چھ تصدیق شدہ ریجنز — وائس سٹی، لیونیڈا کیز، گراس ریورز، پورٹ گیلہورن، ایمبروزیا اور ماؤنٹ کالاگا۔",
f"""
<h1>{E('GTA 6')} کا نقشہ: لیونیڈا</h1>
<p class="lead">{E('GTA 6')} فرضی ریاست <b>لیونیڈا</b> میں ہے، جو امریکی ریاست فلوریڈا سے متاثر ہے۔ {E('Rockstar')} نے چھ ریجنز کی تصدیق کی ہے۔</p>
<p class="updated">آخری اپڈیٹ: {TODAY}</p>
<div class="note">{E('Rockstar')} نے ابھی تک مکمل نقشہ یا اس کا سائز سرکاری طور پر جاری نہیں کیا۔ انٹرنیٹ پر موجود "لیکڈ" نقشے فینز کے بنائے ہوئے اندازے ہیں۔</div>
{AD}
<div class="grid">{rc}</div>
<p style="margin-top:16px">کیا آپ نے سب ریجنز دیکھ لیے؟ <a href="tracker.html">ٹریکر میں ٹک کریں</a>۔</p>
{AD}
""")

# ---------------- EDITIONS ----------------
PAGES["editions.html"] = ("GTA 6 کی قیمت اور ایڈیشن — اسٹینڈرڈ یا الٹیمیٹ؟",
"جی ٹی اے 6 کی قیمت: اسٹینڈرڈ ایڈیشن 79.99 ڈالر اور الٹیمیٹ ایڈیشن 99.99 ڈالر۔ کون سا ایڈیشن آپ کے لیے بہتر ہے؟",
f"""
<h1>{E('GTA 6')} کی قیمت اور ایڈیشن</h1>
<p class="lead">{E('GTA 6')} دو ایڈیشنز میں آیا ہے۔ دونوں میں جیسن اور لوسیا کی پوری کہانی شامل ہے۔</p>
<p class="updated">آخری اپڈیٹ: {TODAY}</p>
<table>
<tr><th>ایڈیشن</th><th>{E('US')}</th><th>{E('UK')}</th></tr>
<tr><td>اسٹینڈرڈ</td><td class="en">$79.99</td><td class="en">£69.99</td></tr>
<tr><td>الٹیمیٹ</td><td class="en">$99.99</td><td class="en">£89.99</td></tr>
</table>
{AD}
<h2>کون سا خریدیں؟</h2>
<div class="grid">
<div class="card"><h3>اسٹینڈرڈ لیں اگر…</h3><p>آپ صرف کہانی کھیلنا چاہتے ہیں اور پیسے بچانا چاہتے ہیں۔ پوری مین اسٹوری اسی میں ہے۔</p></div>
<div class="card"><h3>الٹیمیٹ لیں اگر…</h3><p>آپ اضافی بونس آئٹمز چاہتے ہیں اور 20 ڈالر زیادہ خرچ کر سکتے ہیں۔ بونس کی مکمل تفصیل اپنے اسٹور کے پیج پر دیکھیں۔</p></div>
</div>
<h2>پاکستان سے کیسے خریدیں؟</h2>
<ul>
<li>{E('PlayStation Store')} پاکستان میں سرکاری طور پر دستیاب نہیں، اس لیے لوگ عام طور پر {E('UAE')}، سعودی یا {E('US')} اکاؤنٹ استعمال کرتے ہیں۔</li>
<li>اپنے اکاؤنٹ کے ریجن والا گفٹ کارڈ صرف بھروسے والے دکاندار سے خریدیں۔</li>
<li>بہت سستے "اکاؤنٹ شیئرنگ" یا "پرائمری/سیکنڈری" آفرز سے ہوشیار رہیں — ان میں اکاؤنٹ بند ہونے اور فراڈ کا خطرہ ہوتا ہے۔</li>
<li>باکس والی کاپی میں ڈسک نہیں بلکہ ڈاؤن لوڈ کوڈ ہوتا ہے، پھر بھی پورا گیم انٹرنیٹ سے ڈاؤن لوڈ کرنا پڑے گا۔</li>
</ul>
<div class="note">قیمتیں ڈالر اور پاؤنڈ میں ہیں۔ روپے میں قیمت گفٹ کارڈ کے ریٹ پر منحصر ہے جو روز بدلتا ہے۔</div>
{AD}
""")

# ---------------- TRACKER ----------------
TR_JS = """<script>
(function(){
  var LISTS = {
    prep:['گیم پری لوڈ کر لیا (تقریباً 210 GB)','کنسول سسٹم اپڈیٹ کر لیا','اسٹوریج میں کافی جگہ خالی کر لی','ریسٹ موڈ میں انٹرنیٹ آن رکھا','لوڈ شیڈنگ کے لیے UPS تیار','اپنے ریجن کا ان لاک ٹائم چیک کر لیا'],
    regions:['وائس سٹی','لیونیڈا کیز','گراس ریورز','پورٹ گیلہورن','ایمبروزیا','ماؤنٹ کالاگا نیشنل پارک'],
    people:['لوسیا کامینوس','جیسن ڈووال','کیل ہیمپٹن','برائن ہیڈر','بوبی آئیک','ڈری کوان پریسٹ','ریئل ڈائمز','راؤل بوتیستا']
  };
  var KEY='gta6urdu-tracker-v1', state={};
  try { state = JSON.parse(localStorage.getItem(KEY)) || {}; } catch(e){ state = {}; }
  function save(){ try { localStorage.setItem(KEY, JSON.stringify(state)); } catch(e){} }
  function render(id){
    var box=document.getElementById(id), items=LISTS[id], done=0; box.innerHTML='';
    items.forEach(function(t,i){
      var k=id+'-'+i, on=!!state[k]; if(on) done++;
      var l=document.createElement('label'); l.className='check'+(on?' done':'');
      var c=document.createElement('input'); c.type='checkbox'; c.checked=on;
      c.onchange=function(){ state[k]=c.checked; save(); render(id); total(); };
      var s=document.createElement('span'); s.textContent=t;
      l.appendChild(c); l.appendChild(s); box.appendChild(l);
    });
    document.getElementById(id+'-n').textContent = done+' / '+items.length;
  }
  function total(){
    var all=0, d=0;
    for (var id in LISTS){ LISTS[id].forEach(function(_,i){ all++; if(state[id+'-'+i]) d++; }); }
    var p=Math.round(d*100/all);
    document.getElementById('bar').style.width=p+'%';
    document.getElementById('pct').textContent=p+'%';
  }
  for (var id in LISTS) render(id);
  total();
  document.getElementById('reset').onclick=function(){ state={}; save(); for (var id in LISTS) render(id); total(); };
})();
</script>"""

def tblock(id, title):
    return f'<div class="card"><h3>{title} <span class="tag en" id="{id}-n"></span></h3><div id="{id}"></div></div>'

PAGES["tracker.html"] = ("GTA 6 پروگریس ٹریکر — اپنی پیش رفت ٹک کریں",
"جی ٹی اے 6 پروگریس ٹریکر اردو میں: لانچ کی تیاری، لیونیڈا کے ریجنز اور کردار — ٹک کریں، آپ کی پیش رفت آپ کے فون میں محفوظ رہتی ہے۔",
f"""
<h1>{E('GTA 6')} پروگریس ٹریکر</h1>
<p class="lead">جو کام ہو جائے اسے ٹک کریں۔ آپ کی پیش رفت اسی براؤزر میں محفوظ رہتی ہے — کوئی اکاؤنٹ نہیں چاہیے۔</p>
<div class="card">
<h3>کل پیش رفت: <span class="en" id="pct">0%</span></h3>
<div class="progress"><div id="bar"></div></div>
</div>
{AD}
<div class="grid" style="margin-top:14px">
{tblock('prep','لانچ کی تیاری')}
{tblock('regions','ریجنز جو دیکھ لیے')}
{tblock('people','کردار جن سے ملاقات ہوئی')}
</div>
<p style="margin-top:14px"><button id="reset">سب صاف کریں</button></p>
<div class="note">گیم آنے کے بعد اس ٹریکر میں مشنز، کلیکٹیبلز اور 100% کمپلیشن کی لسٹیں شامل کی جائیں گی۔</div>
{AD}
""", TR_JS)

# ---------------- FAQ ----------------
faqs = [
 (f"کیا {E('GTA 6')} {E('PS4')} پر آئے گا؟", f"نہیں۔ یہ صرف {E('PS5')} (بشمول {E('PS5 Pro')}) اور {E('Xbox Series X|S')} پر ہے۔"),
 (f"کیا {E('GTA 6')} {E('PC')} پر ہے؟", f"ابھی تک {E('PC')} ورژن کا کوئی اعلان نہیں ہوا۔ پچھلی گیمز کی طرح یہ بعد میں آ سکتا ہے، مگر کوئی تاریخ تصدیق شدہ نہیں۔"),
 (f"کیا لانچ پر {E('GTA Online')} ہوگا؟", "گیم سنگل پلیئر تجربے کے طور پر لانچ ہو رہی ہے۔ آن لائن موڈ کی تفصیل بعد میں آنی ہے۔"),
 ("ڈاؤن لوڈ سائز کتنا ہے؟", f"تقریباً {E('210 GB')}۔ اپنے کنسول میں اس سے زیادہ جگہ خالی رکھیں کیونکہ اپڈیٹس بھی آئیں گی۔"),
 ("کیا باکس میں ڈسک ہے؟", "نہیں، باکس میں ڈاؤن لوڈ کوڈ ہوتا ہے۔ گیم انٹرنیٹ سے ڈاؤن لوڈ کرنی پڑے گی۔"),
 ("کیا مرکزی کرداروں کے درمیان سوئچ کر سکتے ہیں؟", "جی ہاں، گیم میں جیسن اور لوسیا دونوں کھیلنے کے قابل کردار ہیں۔"),
 ("مفت میں یا سستا لینے کا کوئی طریقہ ہے؟", "\"مفت GTA 6\"، کریکڈ ورژن یا منی گلچ بیچنے والے لنکس اکثر فراڈ یا وائرس ہوتے ہیں۔ صرف سرکاری اسٹور سے خریدیں۔"),
]
fq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)
PAGES["faq.html"] = ("GTA 6 سوال و جواب — PS4، PC، آن لائن اور مزید",
"جی ٹی اے 6 کے بارے میں عام سوال: کیا یہ PS4 یا PC پر ہے؟ آن لائن موڈ؟ ڈاؤن لوڈ سائز؟ سب کے جواب اردو میں۔",
f"""
<h1>{E('GTA 6')} سوال و جواب</h1>
<p class="updated">آخری اپڈیٹ: {TODAY}</p>
{fq}
{AD}
""")

# ---------------- LEGAL ----------------
PAGES["about.html"] = ("ہمارے بارے میں", "GTA 6 اردو گائیڈ کے بارے میں۔", f"""
<h1>ہمارے بارے میں</h1>
<p>{SITE} پاکستان اور دنیا بھر کے اردو بولنے والے گیمرز کے لیے ایک فین ویب سائٹ ہے۔ ہمارا مقصد {E('GTA 6')} کی درست اور تازہ معلومات آسان اردو میں دینا ہے۔</p>
<p>ہم صرف وہی معلومات شائع کرتے ہیں جو {E('Rockstar Games')} یا قابلِ اعتماد ذرائع سے تصدیق شدہ ہوں، اور افواہوں کو واضح طور پر الگ لکھتے ہیں۔</p>
<p>یہ سائٹ {E('Rockstar Games')} یا {E('Take-Two Interactive')} سے منسلک نہیں ہے۔</p>
""")
PAGES["privacy.html"] = ("پرائیویسی پالیسی", "GTA 6 اردو گائیڈ کی پرائیویسی پالیسی۔", f"""
<h1>پرائیویسی پالیسی</h1>
<p class="updated">آخری اپڈیٹ: {TODAY}</p>
<p>ہم آپ سے کوئی ذاتی معلومات (نام، ای میل وغیرہ) جمع نہیں کرتے۔ پروگریس ٹریکر کا ڈیٹا صرف آپ کے اپنے براؤزر میں محفوظ ہوتا ہے اور ہمارے سرور پر نہیں آتا۔</p>
<h2>اشتہارات اور کوکیز</h2>
<p>یہ سائٹ {E('Google AdSense')} کے اشتہارات دکھا سکتی ہے۔ {E('Google')} سمیت تیسرے فریق کے وینڈرز کوکیز استعمال کرتے ہیں تاکہ آپ کی اس اور دیگر ویب سائٹس پر پچھلی وزٹس کی بنیاد پر اشتہار دکھائے جا سکیں۔ آپ {E('Google')} کی <a href="https://adssettings.google.com" rel="nofollow">ایڈ سیٹنگز</a> میں ذاتی نوعیت کے اشتہارات بند کر سکتے ہیں۔</p>
<h2>رابطہ</h2>
<p>کسی بھی سوال کے لیے <a href="contact.html">رابطہ</a> پیج دیکھیں۔</p>
<hr>
<div class="en" dir="ltr">
<h2>Privacy Policy (English)</h2>
<p>We do not collect personal information. Tracker data is stored only in your browser's local storage. This site may display Google AdSense ads. Third-party vendors, including Google, use cookies to serve ads based on your prior visits to this and other websites. You can opt out of personalised advertising at <a href="https://adssettings.google.com" rel="nofollow">Google Ads Settings</a>.</p>
</div>
""")
PAGES["contact.html"] = ("رابطہ", "GTA 6 اردو گائیڈ سے رابطہ کریں۔", f"""
<h1>رابطہ</h1>
<p>کوئی غلطی نظر آئے، تجویز ہو یا کاروباری بات کرنی ہو تو ای میل کریں:</p>
<p class="big en">YOUR-EMAIL@example.com</p>
""")

def main():
    os.makedirs(OUT, exist_ok=True)
    shutil.copy(os.path.join(os.path.dirname(__file__), "style.css"), OUT)
    for fname, spec in PAGES.items():
        title, desc, body, *js = spec
        with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
            f.write(page(fname, title, desc, body, js[0] if js else ""))
    urls = "".join(
        f"<url><loc>{DOMAIN}/{'' if f == 'index.html' else f}</loc><lastmod>{ISO}</lastmod></url>\n"
        for f in PAGES)
    with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
    with open(os.path.join(OUT, "robots.txt"), "w") as f:
        f.write(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
    with open(os.path.join(OUT, "ads.txt"), "w") as f:
        f.write("# After AdSense approval replace with: google.com, pub-XXXXXXXXXXXXXXXX, DIRECT, f08c47fec0942fa0\n")
    print("built", len(PAGES), "pages")

if __name__ == "__main__":
    main()

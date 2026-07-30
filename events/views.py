from django.shortcuts import render


def home(request):
    # مدخلات نصية تحتمل وجود مسافات أو حروف صغيرة
    raw_course = "software engineering"
    raw_developer = "   المهندسة حسناء   "
    raw_semester = "second semester"
    
    # تطبيق دوال النصوص والحسابات خلف الكواليس
    context = {
        "course_name": raw_course.title(),           # تحويل إلى: Software Engineering
        "developer": raw_developer.strip(),          # إزالة المسافات الزائدة من الأطراف
        "university": "Yemen University".upper(),     # تحويل لحروف كبيرة: YEMEN UNIVERSITY
        "semester": raw_semester.capitalize(),       # تكبير أول حرف فقط
        "year": 2026,
        "visitors": 150 + 50,                        # إمكانية إجراء حسابات مباشرة
    }

    return render(request, "events/home.html", context)


def event_list(request):
    # قائمة البيانات الخام
    raw_events = [
        {
            "name": "  ملتقى التقنية والذكاء الاصطناعي  ",
            "category": "technology",
            "location": "صنعاء",
            "price": "free"
        },
        {
            "name": "ورشة تطوير المهارات البرمجية",
            "category": "education",
            "location": "عدن",
            "price": "1000 ريال"
        },
        {
            "name": "معرض المشاريع الهندسية",
            "category": "innovation",
            "location": "تعز",
            "price": "free"
        }
    ]

    # معالجة كل عنصر داخل القائمة بشكل مستقل
    cleaned_events = []
    for item in raw_events:
        cleaned_events.append({
            "name": item["name"].strip(),                                   # تنظيف المسافات
            "category": item["category"].upper(),                           # تحويل النص لحروف كبيرة
            "location": item["location"],
            "price": "مجاني" if item["price"].lower() == "free" else item["price"] # تحويل كلمة free إلى مجاني
        })

    context = {
        "events": cleaned_events
    }

    return render(request, "events/event_list.html", context)
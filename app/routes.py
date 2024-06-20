from flask import render_template, flash, redirect, url_for
from . import create_app, db  # Импортируем функцию create_app и объект db из текущего пакета

app = create_app()  # Создаем экземпляр приложения Flask


# Маршрут для отображения главной страницы
@app.route('/')
def index():
    # Получаем все наушники из базы данных
    headphones = Headphone.query.all()
    # Отображаем шаблон index.html, передавая ему заголовок страницы и список наушников
    return render_template('index.html', title='Главная', headphones=headphones)


# Маршрут для добавления новых наушников
@app.route('/add', methods=['GET', 'POST'])
def add_headphone():
    # Создаем экземпляр формы для добавления наушников
    form = AddHeadphoneForm()
    # Если форма была отправлена методом POST и прошла валидацию
    if form.validate_on_submit():
        # Создаем новый объект Headphone на основе данных из формы
        headphone = Headphone(name=form.name.data, description=form.description.data,
                              price=form.price.data, image_url=form.image_url.data)
        # Добавляем новый наушник в базу данных
        db.session.add(headphone)
        # Применяем изменения к базе данных
        db.session.commit()
        # Выводим сообщение об успешном добавлении наушника
        flash('Наушники добавлены!')
        # Перенаправляем пользователя на главную страницу
        return redirect(url_for('index'))
    # Если форма не была отправлена или не прошла валидацию, отображаем шаблон add_headphone.html
    # и передаем ему заголовок страницы и объект формы
    return render_template('add_headphone.html', title='Добавить наушники', form=form)

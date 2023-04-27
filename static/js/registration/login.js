$(document).ready(function() {
      // Функция, которая вызывается при отправке формы логина
      $('form').submit(function(event) {
        event.preventDefault(); // Останавливаем отправку формы
        var username = $('#id_username').val(); // Получаем значение логина пользователя
        var password = $('#id_password').val(); // Получаем значение пароля пользователя

    // AJAX-запрос на сервер для проверки учетных данных пользователя
      $.ajax({
      url: '/login/', // URL-адрес для отправки запроса
      type: 'POST', // Метод запроса (GET или POST)
      data: { // Данные, отправляемые на сервер
        'username': username,
        'password': password,
        'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
      },
      success: function(response) { // Функция, вызываемая при успешной отправке запроса
        if (response.success) { // Если авторизация прошла успешно
          window.location.href = '/'; // Перенаправляем пользователя на главную страницу
        } else { // Если авторизация не удалась
          $('#error-message').text('Неверное имя пользователя или пароль.'); // Выводим сообщение об ошибке
        }
      },
      error: function(response) { // Функция, вызываемая при ошибке отправки запроса
        $('#error-message').text('Произошла ошибка при отправке запроса на сервер.'); // Выводим сообщение об ошибке
      }
    });
  });

});

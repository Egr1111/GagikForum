$(function () {
  $(".marquee").marquee({
    //если хотите всегда анимировать при помощи jQuery
    allowCss3Support: true,

    //работает, когда allowCss3Support установлено в true - смотрите полный список http://www.w3.org/TR/2013/WD-css3-transitions-20131119/#transition-timing-function
    css3easing: "linear",

    //требует jQuery easing плагин. По умолчанию - 'linear'
    easing: "linear",

    //приостанавливает время перед стартом следующей анимации в миллисекундах
    delayBeforeStart: 0,
    //'left', 'right', 'up' or 'down'
    direction: "left",

    //true или false - должен ли marquee быть дублирован для эффекта продолжающегося потока
    duplicated: false,

    //скорость marquee в миллисекундах
    duration: 7000,

    //расстояние в пикселях между бегущими строками
    gap: 20,

    //приостанавливает цикл marquee
    pauseOnCycle: false,

    //приостанавливает marquee при наведении курсора мыши - используя плагин jQuery https://github.com/tobia/Pause
    pauseOnHover: false,

    //marquee виден, когда он изначально позиционирован у границы по направлении которой будет двигаться startVisible: false
  });
});

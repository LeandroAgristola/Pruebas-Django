const video = document.getElementById('myVideo');

// Configura el inicio del video a los 10 segundos
video.currentTime = 13;

// Reproduce el video cuando está listo
video.play();

// Detén el video en el segundo 63 y luego reinícialo
video.addEventListener('timeupdate', function() {
    if (video.currentTime >= 63) {
        video.currentTime = 13;  // Reinicia el video a los 10 segundos
        video.play();  // Reproduce el video nuevamente
    }
});
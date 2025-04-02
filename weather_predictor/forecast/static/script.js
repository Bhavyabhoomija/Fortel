document.addEventListener("DOMContentLoaded", function () {
    // Get the weather condition from a hidden element in the HTML
    let weatherCondition = document.getElementById("weatherCondition")?.textContent.trim();

    if (weatherCondition) {
        updateBackground(weatherCondition);
    }
});

function updateBackground(weatherCondition) {
    const body = document.body;

  
    const backgrounds = {
        "clear sky": "url('/static/images/clear.jpg')",
        "few clouds": "url('/static/images/cloudy.jpg')",
        "broken clouds": "url('/static/images/cloudy.jpg')",
        "light rain": "url('/static/images/Rainy.jpg')",
        "heavy rain":"url('/static/images/Rainy.jpg')",
        "snow": "url('/static/images/snow.jpg')",
        "thunderstorm": "url('/static/images/stormy.jpg')",
        "sunny": "url('/static/images/sunny.jpg')",
        "default":"url('/static/images/clear_sky.jpg')"
    };

   
    body.style.backgroundImage = backgrounds[weatherCondition] || backgrounds["default"];
    body.style.backgroundSize = "cover";
    body.style.backgroundPosition = "center";
}

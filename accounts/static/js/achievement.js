const counters = document.querySelectorAll('.counter');

const observer = new IntersectionObserver((entries, observer) => {

    entries.forEach(entry => {

        if (entry.isIntersecting) {

            const counter = entry.target;
            const target = +counter.getAttribute('data-target');

            let count = 0;
            const speed = 30;

            const updateCounter = () => {

                const increment = target / 100;

                if (count < target) {

                    count += increment;

                    counter.innerText = Math.ceil(count);

                    setTimeout(updateCounter, speed);

                } else {

                    counter.innerText = target;

                }
            };

            updateCounter();

            observer.unobserve(counter);
        }

    });

}, {
    threshold: 0.5
});

counters.forEach(counter => {
    observer.observe(counter);
});
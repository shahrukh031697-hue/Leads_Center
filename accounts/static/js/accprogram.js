const moduleHeaders =
    document.querySelectorAll(".module-header");


moduleHeaders.forEach(header => {

    header.addEventListener("click", () => {

        const currentBox =
            header.parentElement;


        document
            .querySelectorAll(".module-box")
            .forEach(box => {

                if (box !== currentBox) {

                    box.classList.remove("active");

                }

            });


        currentBox.classList.toggle("active");

    });

});
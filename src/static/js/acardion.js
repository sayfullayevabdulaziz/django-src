const moCardHeader = document.querySelectorAll('.mo-card-header');
const moCardHeaderButtonLine = document.querySelectorAll('.mo-card-header-button-line');
const moCardBody = document.querySelectorAll('.mo-card-body');
moCardHeader.forEach((item, index) => {
    item.addEventListener('click', () => {
        moCardHeaderButtonLine.forEach((el, idx) => {
            if (index === idx) {
                el.classList.toggle('mo-active');
            }
        });
        moCardBody.forEach((el, idx) => {
            if (index === idx) {
                el.classList.toggle('mo-visible');
            }
        });
    });
});

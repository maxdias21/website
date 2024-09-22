const inputPassword = document.querySelector('#password');
const spanPassword = document.querySelector('#help-password');

const inputUsername = document.querySelector('#username');
const spanUsername = document.querySelector('#help-username');

const inputButton = document.querySelector('#btn');

inputPassword.addEventListener('input', () => {
    validation({
        inputValue: inputPassword.value,
        spanElement: spanPassword,
        sequential: true,
        onlyNumbers: true
    });
});

inputUsername.addEventListener('input', () => hasValue({
    inputValue: inputUsername.value,
    spanElement: spanUsername,
    emptyValue: 'O campo usuário não pode ficar vazio.'
}));

function hasValue({inputValue, spanElement, emptyValue}) {
    const defaultEmptyValue = 'Campo obrigatório'

    if(inputValue.length === 0) {
        addTextOnContainer(spanElement, emptyValue || defaultEmptyValue)
        addErrorClass(spanElement)
    } else {
        addTextOnContainer(spanElement, ' ')
    }
}

function validation({
    inputValue,
    spanElement,
    minLengthValue =6,
    errorMessageField,
    successMessageField,
    successMessageWarning,
    sequential= false,
    onlyNumbers = false }) {

    const defaultMessageSequential = 'Recomendação: Evite usar números em sequência.';
    const defaultMessageIsOnlyNumbers = 'Recomendação: Evite usar apenas números.';
    const defaultSuccessMessage = 'Campo válido!';
    const defautlErrorMessage = 'Campo inválido!';
    const defaultSuccessWarningMessage = 'Campo válido, mas não atende às nossas recomendações!';

    let hasError = false;
    let hasPassed = minLength(inputValue, minLengthValue);

    if(!hasPassed) {
        addTextOnContainer(spanElement, errorMessageField || defautlErrorMessage);
        addErrorClass(spanElement);
    }

    if(sequential && sequentialPattern(inputValue)) {
        addErrorClass(spanElement);
        addTextOnContainer(spanElement, sequential.message || defaultMessageSequential);
        hasError = true;
    }

    if (onlyNumbers && isOnlyNumbers(inputValue)) {
        addErrorClass(spanElement);
        addTextOnContainer(spanElement, isOnlyNumbers.message || defaultMessageIsOnlyNumbers);
        hasError = true;
    }

    if(hasPassed) {
        addSuccessClass(spanElement);

        if(hasError) {
            addTextOnContainer(spanElement, successMessageWarning || defaultSuccessWarningMessage);
        return
        }

        addTextOnContainer(spanElement, successMessageField || defaultSuccessMessage);
        return;
    }
}

function addTextOnContainer(container, text) {
    container.textContent = text;
}

function addErrorClass(spanElement) {
    spanElement.classList.add('error');
    spanElement.classList.remove('success');
}

function addSuccessClass() {
    spanPassword.classList.add('success');
    spanPassword.classList.remove('error');
}

function sequentialPattern(value) {
    return  /(012|123|234|345|456|567|678|789|890)/.test(value);
}

function isOnlyNumbers(text) {
    return  /^\d+$/.test(text);
}

function minLength(text, minLength=6) {
    return text.length >= minLength;
}


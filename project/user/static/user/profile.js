const showUpdateProfileFormButton = document.querySelector('#show-update-profile-form-button');
const hideUpdateProfileFormButton = document.querySelector('#hide-update-profile-form-button')
const updateProfileForm = document.querySelector('#update-profile-form');

loadEventListeners();

function loadEventListeners()
{
    document.addEventListener('DOMContentLoaded', profilePage);
    showUpdateProfileFormButton.addEventListener('click', showUpdateProfileForm);
    hideUpdateProfileFormButton.addEventListener('click', hideUpdateProfileForm);
}

function profilePage()
{
    updateProfileForm.style.display = 'none';
}

function showUpdateProfileForm()
{
    showUpdateProfileFormButton.style.display = 'none';
    updateProfileForm.style.display = 'block';
}

function hideUpdateProfileForm()
{
    showUpdateProfileFormButton.style.display = 'block';
    updateProfileForm.style.display = 'none';
}
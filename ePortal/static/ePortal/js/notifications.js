window.addEventListener('DOMContentLoaded', function () {
    const notificationsList = document.getElementById('notifications-list');

    function getNotifications() {
        fetch('/get-notifications/')  
            .then(response => response.json())
            .then(data => {
                // Oczyszczanie listy tylko, gdy są nowe powiadomienia
                if (data.notifications.length > 0) {
                    notificationsList.innerHTML = '';  // Wyczyść istniejące powiadomienia
                    data.notifications.forEach(notification => {
                        const listItem = document.createElement('li');
                        listItem.innerHTML = `<a class="dropdown-item" href="#">${notification.content}</a>`;
                        notificationsList.appendChild(listItem);
                    });
                } else {
                    // Sprawdź, czy już istnieje informacja o braku powiadomień
                    const existingNoNotificationsItem = notificationsList.querySelector('.no-notifications-item');
                
                    if (!existingNoNotificationsItem) {
                        // Dodaj informację o braku powiadomień
                        const noNotificationsItem = document.createElement('li');
                        noNotificationsItem.className = 'no-notifications-item';
                        noNotificationsItem.innerHTML = '<span class="text-muted">Brak nowych powiadomień</span>';
                        notificationsList.appendChild(noNotificationsItem);
                    }
                }  
            });
    }

    getNotifications(); 
    setInterval(getNotifications, 30000);

    const dropdownToggle = document.querySelector('.navbar .dropdown-toggle');
    const dropdownMenu = document.querySelector('.navbar .dropdown-menu');

    dropdownToggle.addEventListener('click', function (event) {
        event.preventDefault();

        const isExpanded = dropdownMenu.classList.contains('show');
        if (!isExpanded) {
            dropdownMenu.classList.add('show');
        } else {
            dropdownMenu.classList.remove('show');
        }
    });

    const toastTrigger = document.getElementById('liveToastBtn')
    const toastLiveExample = document.getElementById('liveToast')

    if (toastTrigger) {
        const toastBootstrap = new bootstrap.Toast(toastLiveExample);
        toastTrigger.addEventListener('click', () => {
            toastBootstrap.show()
        })
    }
});

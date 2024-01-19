$(document).ready(function () {
    $('#wniosekSelect').on('change', function () {
        var selectedOption = $(this).val();

        switch (selectedOption) {
            case '1':
                $('#wniosekContent').html('<h3>Złóż wniosek - Ogólny</h3>');

                $('#wniosekContent').append(`
                <form class="was-validated">
                <div class="mb-3">
                  <label for="validationTextarea" class="form-label"></label>
                  <textarea class="form-control" id="validationTextarea" placeholder="Wymagane" required></textarea>
                  <div class="invalid-feedback">
                    Wiadomość jest wymagana
                  </div>
                </div>
              
                <div class="form-check mb-3">
                  <input type="checkbox" class="form-check-input" id="validationFormCheck1" required>
                  <label class="form-check-label" for="validationFormCheck1">Potwierdzam treść wniosku</label>
                  <div class="invalid-feedback"></div>
                </div>
              
                <div class="mb-3">
                  <select class="form-select" required aria-label="select example">
                    <option value="">Wybierz dział</option>
                    <option value="1">Kadry</option>
                    <option value="2">Przełożony</option>
                    <option value="3">Lorem ipsum</option>
                  </select>
                  <div class="invalid-feedback">Należy wskazać dział</div>
                </div>
              
                <div class="mb-3">
                  <input type="file" class="form-control" aria-label="file example">
                  <div class="invalid-feedback">Nieprawidłowy format</div>
                </div>
              
                <div class="mb-3">
                  <button class="btn btn-light" type="submit">Wyślij</button>
                </div>
                <div class="mb-3">
                <a class="btn btn-light" href="/form/" role="button">Cofnij</a>
              </div>
              </form>
                `);
                break;
                case '2':
                  $('#wniosekContent').html('<h3>Złóż wniosek - Zmiana danych</h3>');
              
                  $('#wniosekContent').append(`
                  <form class="row g-3 needs-validation was-validated" novalidate>
                  <div class="col-md-4">
                    <label for="validationCustom01" class="form-label">Imię</label>
                    <input type="text" class="form-control" id="validationCustom01" placeholder="Imię" required>
                  </div>
                  <div class="col-md-4">
                    <label for="validationCustom02" class="form-label">Nazwisko</label>
                    <input type="text" class="form-control" id="validationCustom02" placeholder="Nazwisko" required>
                  </div>
                  <div class="col-md-4">
                    <label for="validationCustomUsername" class="form-label">Adres email</label>
                    <div class="input-group has-validation">
                      <span class="input-group-text" id="inputGroupPrepend">@</span>
                      <input type="text" class="form-control" id="validationCustomUsername" aria-describedby="inputGroupPrepend" placeholder="email@email.pl" required>
                    </div>
                  </div>
                  <div class="col-md-6">
                    <label for="validationCustom03" class="form-label">Miasto</label>
                    <input type="text" class="form-control" id="validationCustom03" placeholder="Miasto" required>
                  </div>
                  <div class="col-md-3">
                    <label for="validationCustom04" class="form-label">Województwo</label>
                    <select class="form-select" id="validationCustom04" required>
                      <option selected disabled value="">Wybierz</option>
                      <option>lorem ipsum<option>
                    </select>
                  </div>
                  <div class="col-md-3">
                    <label for="validationCustom05" class="form-label">Kod pocztowy</label>
                    <input type="text" class="form-control" id="validationCustom05" placeholder="Kod pocztowy" required>
                  </div>
                  <div class="col-12">
                    <div class="form-check">
                      <input class="form-check-input" type="checkbox" value="" id="validationFormCheck1" required>
                      <label class="form-check-label" for="validationFormCheck1">
                        Potwierdzam poprawność danych
                      </label>
                      <div class="invalid-feedback">
                        Musisz potwierdzić poprawność danych przed wysłaniem
                      </div>
                    </div>
                  </div>
                  <div class="col-12">
                    <button class="btn btn-light" type="submit">Wyślij</button>
                  </div>
                  <div class="mb-3">
                  <a class="btn btn-light" href="/form/" role="button">Cofnij</a>
                </div>
                </form>
                  `);
                  break;
            case '3':
                $('#wniosekContent').html('<h3>Złóż wniosek - Lorem ipsum</h3><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis faucibus convallis dolor, a molestie neque fringilla non. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras a augue quis elit interdum sollicitudin eu nec elit. Pellentesque luctus dignissim nibh non vehicula. Nunc scelerisque, sapien ut egestas efficitur, ipsum lacus auctor orci, quis ultricies nisi sem sed velit. Vivamus dictum convallis interdum. Vivamus quam massa, sollicitudin sed sagittis id, condimentum eu lectus. Donec ornare quam sit amet ante aliquet, sit amet sodales lorem convallis. Nullam sit amet tellus eget lacus tempor fringilla.</p>');
                break;
            default:
                $('#wniosekContent').html('<h3>Złóż wniosek</h3>');
        }
    });
});

function allData() {

    // Отримання значення поля з ідентифікатором sellOption
    var sellOptionValue = document.getElementById("sellOption").value;
    console.log("sellOption value:", sellOptionValue);

    // Отримання значення поля з ідентифікатором rentOption
    var rentOptionValue = document.getElementById("rentOption").value;
    console.log("rentOption value:", rentOptionValue);

    // Отримання значення поля з ідентифікатором bothOption
    var bothOptionValue = document.getElementById("bothOption").value;
    console.log("bothOption value:", bothOptionValue);

    // Отримання значення поля з ідентифікатором ptypes
    var ptypesValue = document.getElementById("ptypes").value;
    console.log("ptypes value:", ptypesValue);

    // Отримання значення поля з ідентифікатором yesOption
    var yesOptionValue = document.getElementById("yesOption").value;
    console.log("yesOption value:", yesOptionValue);

    // Отримання значення поля з ідентифікатором noOption
    var noOptionValue = document.getElementById("noOption").value;
    console.log("noOption value:", noOptionValue);

    // Отримання значення поля з ідентифікатором NextId1Name
    var NextId1NameValue = document.getElementById("NextId1Name").value;
    console.log("NextId1Name value:", NextId1NameValue);

}

                function incrementFormNum(event) {
                    event.preventDefault();
                    var formNumInput = document.getElementById('form_num');
                    formNumInput.value = parseInt(formNumInput.value) + 1;
                    document.getElementById('startId').style.display = 'none';
                    document.getElementById('NextId1').style.display = 'block';
                }

                function incrementFormNum1(event, projectNames) {
                    event.preventDefault();

                    var propertyType = document.querySelector('input[name="propertyType"]:checked');
                    var selectedPropertyType = document.getElementById('ptypes').value;
                    var IsName = document.querySelector('input[name="IsName"]:checked');
                    var isNameYes = document.getElementById('yesOption').checked;
                    var developmentName = document.getElementsByName('NextId1Name')[0].value.trim();

                    var projectNamesInput = document.getElementById('projectNames');
                    var projectNamesValue = projectNamesInput.value;
                    var projectNamesArray = projectNamesValue.split(',');


                    if (!propertyType) {
                        document.getElementById('messages-container-propertyType').style.display = 'block';
                        return;
                    }
                    document.getElementById('messages-container-propertyType').style.display = 'none';


                    if (selectedPropertyType === '') {
                        document.getElementById('messages-container-ptypes').style.display = 'block';
                        return;
                        }
                    document.getElementById('messages-container-ptypes').style.display = 'none';


                    if (!IsName && document.getElementById('NextId1IsName').style.display === 'block') {
                        document.getElementById('messages-container-IsName').style.display = 'block';
                        return;
                    }
                    document.getElementById('messages-container-IsName').style.display = 'none';


                    if (isNameYes && developmentName === '' || developmentName === '' && (selectedPropertyType === '3' || selectedPropertyType === '4')) {
                        document.getElementById('messages-container-NextId1Name').style.display = 'block';
                        return;
                    }

                    if (selectedPropertyType === '3') {
                        document.getElementById('outdoor_area').style.display = 'none';
                        document.getElementById('plot_size').style.display = 'none';
                    }
                    else {
                        document.getElementById('outdoor_area').style.display = 'block';
                        document.getElementById('plot_size').style.display = 'block';
                    }

                    if (selectedPropertyType === '1' || selectedPropertyType === '2' || selectedPropertyType === '5' ||selectedPropertyType === '7') {
                        document.getElementById('select_storeys').style.display = 'block';
                    }
                    else {
                        document.getElementById('select_storeys').style.display = 'none';
                    }

                    if ( !isNameYes && (selectedPropertyType === '1' || selectedPropertyType === '2' || selectedPropertyType === '5' ||selectedPropertyType === '7')) {
                        document.getElementById('date').style.display = 'block';
                    }
                    else {
                        document.getElementById('date').style.display = 'none';
                    }

                    if (propertyType.value === 'sell') {
                         document.getElementById('for_rent').style.display = 'none';
                         document.getElementById('for_sale').style.display = 'block';
                         document.getElementById('div-sales_price').style.display = 'block';
                         document.getElementById('div-NextId3step3Year').style.display = 'none';
                    }

                    if (propertyType.value === 'rent') {
                         document.getElementById('for_rent').style.display = 'block';
                         document.getElementById('for_sale').style.display = 'none';
                         document.getElementById('div-sales_price').style.display = 'none';
                         document.getElementById('div-NextId3step3Year').style.display = 'block';
                    }

                    if (propertyType.value === 'both') {
                         document.getElementById('for_rent').style.display = 'block';
                         document.getElementById('for_sale').style.display = 'block';
                         document.getElementById('div-sales_price').style.display = 'block';
                         document.getElementById('div-NextId3step3Year').style.display = 'block';
                    }



                    document.getElementById('messages-container-NextId1Name').style.display = 'none';

                    console.log(projectNamesArray.includes(developmentName))
                    console.log(developmentName)
                    console.log(projectNamesArray)

                    if (projectNamesArray.includes(developmentName)) {
                        var formNumInput = document.getElementById('form_num');
                        formNumInput.value = parseInt(formNumInput.value) + 1;
                        document.getElementById('NextId1').style.display = 'none';
                        document.getElementById('NextId3').style.display = 'block';
                        return;
                    }

                    var formNumInput = document.getElementById('form_num');
                    formNumInput.value = parseInt(formNumInput.value) + 1;
                    document.getElementById('NextId1').style.display = 'none';
                    document.getElementById('NextId2').style.display = 'block';
                }

                function incrementFormNum2(event) {
                    event.preventDefault();

                    var regionIn = document.getElementById("region").value;
                    var locationIn1 = document.getElementById("locationBangkok").value;
                    var locationIn2 = document.getElementById("locationTest").value;

                    if (regionIn === '') {
                        document.getElementById('messages-container-region').style.display = 'block';
                        return;
                    }
                    document.getElementById('messages-container-region').style.display = 'none';

                    if (locationIn1 === '' && locationIn2 === '') {
                        document.getElementById('messages-container-location').style.display = 'block';
                        return;
                    }
                    document.getElementById('messages-container-location').style.display = 'none';


                    var formNumInput = document.getElementById('form_num');
                    formNumInput.value = parseInt(formNumInput.value) + 1;
                    document.getElementById('NextId2').style.display = 'none';
                    document.getElementById('NextId3').style.display = 'block';
                }

                function incrementFormNum3(event) {
                    event.preventDefault();

                    var indoorAreaSize = document.getElementById('propertySize').value.trim();

                    if (indoorAreaSize === '') {
                        document.getElementById('messages-container-propertySize').style.display = 'block';
                        return;
                    }

                    var formNumInput = document.getElementById('form_num');
                    formNumInput.value = parseInt(formNumInput.value) + 2;
                    document.getElementById('NextId3').style.display = 'none';
                    document.getElementById('NextId4').style.display = 'block';
                    document.getElementById('messages-container-propertySize').style.display = 'none';
                }

                function incrementFormNum4(event) {
                    event.preventDefault();
                    var formNumInput = document.getElementById('form_num');
                    formNumInput.value = parseInt(formNumInput.value) + 1;
                    document.getElementById('NextId4').style.display = 'none';
                    document.getElementById('NextId5').style.display = 'block';
                }
                function incrementFormNum5(event) {
                    event.preventDefault();
                    var formNumInput = document.getElementById('form_num');
                    formNumInput.value = parseInt(formNumInput.value) + 1;
                    document.getElementById('NextId5').style.display = 'none';
                    document.getElementById('NextId6').style.display = 'block';
                }

                function incrementFormNum6(event) {
                    event.preventDefault();
                    var formNumInput = document.getElementById('form_num');
                    formNumInput.value = parseInt(formNumInput.value) + 1;
                    allData();
                    document.getElementById('NextId6').style.display = 'none';
                    document.getElementById('startId').style.display = 'block';
                }

                function decrementFormNum2(event) {
                    event.preventDefault();
                    var formNumInput = document.getElementById('form_num');
                    formNumInput.value = parseInt(formNumInput.value) - 1;
                    document.getElementById('NextId2').style.display = 'none';
                    document.getElementById('NextId1').style.display = 'block';
                }

                function decrementFormNum3(event) {
                    event.preventDefault();
                    var formNumInput = document.getElementById('form_num');
                    var regionIn = document.getElementById("region").value;
                    if (regionIn === '') {
                        formNumInput.value = parseInt(formNumInput.value) - 2;
                        document.getElementById('NextId3').style.display = 'none';
                        document.getElementById('NextId1').style.display = 'block';
                        return;
                    }
                    formNumInput.value = parseInt(formNumInput.value) - 1;
                    document.getElementById('NextId3').style.display = 'none';
                    document.getElementById('NextId2').style.display = 'block';
                }

                function decrementFormNum4(event) {
                    event.preventDefault();
                    var formNumInput = document.getElementById('form_num');
                    formNumInput.value = parseInt(formNumInput.value) - 1;
                    document.getElementById('NextId4').style.display = 'none';
                    document.getElementById('NextId3').style.display = 'block';
                }

                function decrementFormNum5(event) {
                    event.preventDefault();
                    var formNumInput = document.getElementById('form_num');
                    formNumInput.value = parseInt(formNumInput.value) - 1;
                    document.getElementById('NextId5').style.display = 'none';
                    document.getElementById('NextId4').style.display = 'block';
                }

                function decrementFormNum6(event) {
                    event.preventDefault();
                    var formNumInput = document.getElementById('form_num');
                    formNumInput.value = parseInt(formNumInput.value) - 1;
                    document.getElementById('NextId6').style.display = 'none';
                    document.getElementById('NextId5').style.display = 'block';
                }




// Function to handle property type selection
                  function handlePropertyTypeNextId1() {
                    var propertyTypeSelect = document.getElementById("ptypes");
                    document.getElementById('NextId1IsName').style.display = 'block';

                    var developmentLabel = document.getElementById("NextId1Label2");
                    var developmentLabel1 = document.getElementById("NextId1Label1");
                    var selectedOption = propertyTypeSelect.options[propertyTypeSelect.selectedIndex].text;

                    var isNameYes = document.getElementById('yesOption').checked;


                    if (selectedOption === 'House') {
                        developmentLabel1.textContent = "Is your house part of a housing development or gated community?";

                        document.getElementById('NextId1IsName').style.display = 'block';
                        developmentLabel.textContent = "What is the name of the development where your house is located?";
                    }
                    else if (selectedOption === 'Villa') {
                        developmentLabel1.textContent = "Is your villa part of a housing development or gated community?";
                        document.getElementById('NextId1IsName').style.display = 'block';
                        developmentLabel.textContent = "What is the name of the development where your villa is located?";
                    }
                    else if (selectedOption === 'Condo') {
                        document.getElementById('NextId1IsName').style.display = 'none';
                        document.getElementById('NextId1EnterName').style.display = 'block';
                        developmentLabel.textContent = "What is the name of the project or building where your condo is located?";
                    }
                    else if (selectedOption === 'Apartment') {
                        document.getElementById('NextId1IsName').style.display = 'none';
                        document.getElementById('NextId1EnterName').style.display = 'block';
                        developmentLabel.textContent = "What is the name of the project or building where your apartment is located?";
                    }
                    else if (selectedOption === 'Townhouse') {
                        developmentLabel1.textContent = "Is your townhouse part of a housing development or gated community?";
                        document.getElementById('NextId1IsName').style.display = 'block';
                        developmentLabel.textContent = "What is the name of the development where your townhouse is located?";
                    }
                    else if (selectedOption === 'Land') {
                        developmentLabel1.textContent = "Is your land part of a housing development or gated community?";
                        document.getElementById('NextId1IsName').style.display = 'block';
                        developmentLabel.textContent = "What is the name of the development where your land is located?";
                    }
                    else if (selectedOption === 'Shophouse') {
                        developmentLabel1.textContent = "Is your shophouse part of a housing development or gated community?";
                        document.getElementById('NextId1IsName').style.display = 'block';
                        developmentLabel.textContent = "What is the name of the development where your shophouse is located?";
                    }

                  }

                  // Event listener for property type selection change
                  var propertyTypeSelect = document.getElementById("ptypes");
                  propertyTypeSelect.addEventListener("change", handlePropertyTypeNextId1);



function handlePropertyTypeNextId2() {
    var propertyTypeSelect = document.getElementById("ptypes");
    document.getElementById('NextId1EnterName').style.display = 'block';
}

var propertyTypeSelect = document.getElementById("yesOption");
propertyTypeSelect.addEventListener("change", handlePropertyTypeNextId2);



function handlePropertyTypeNextId3() {
   document.getElementById('NextId1EnterName').style.display = 'none';
   var developmentNameInput = document.getElementsByName("NextId1Name")[0];
    developmentNameInput.value = "";
}

var noOption = document.getElementById("noOption");
noOption.addEventListener("change", handlePropertyTypeNextId3);





let minusBtnBed = document.getElementById("minus-btn-bed");
let countBed = document.getElementById("count-bed");
let plusBtnBed = document.getElementById("plus-btn-bed");

let countNumBed = 0;
countBed.innerHTML = countNumBed;

minusBtnBed.addEventListener("click", () => {
    if (countBed.innerHTML === '1') {
        countBed.innerHTML = 'Studio';
        countNumBed = 0;
    }
    else if (countBed.innerHTML === 'Studio') {
        countBed.innerHTML = 'Studio';
    }
	else {
        countNumBed -= 1;
        countBed.innerHTML = countNumBed;
	}
});

plusBtnBed.addEventListener("click", () => {
    if (countBed.innerHTML === '0') {
        countNumBed = 0;
        countBed.innerHTML = 'Studio';
    }
	else {
        countNumBed += 1;
        countBed.innerHTML = countNumBed;
	}
});







let minusBtnBeth = document.getElementById("minus-btn-bath");
let countBeth = document.getElementById("count-bath");
let plusBtnBeth = document.getElementById("plus-btn-bath");

let countNumBeth = 0;
countBeth.innerHTML = countNumBeth;

minusBtnBeth.addEventListener("click", () => {
    if (countBeth.innerHTML === '1') {
        countNumBeth = 0;
        countBeth.innerHTML = countNumBeth;
    }
    else if (countBeth.innerHTML === '0') {
        countBeth.innerHTML = '0';
    }
	else {
        countNumBeth -= 0.5;
        countBeth.innerHTML = countNumBeth;
	}
});

plusBtnBeth.addEventListener("click", () => {
    if (countBeth.innerHTML === '0') {
        countNumBeth = 1;
        countBeth.innerHTML = countNumBeth;
        return;
    }
	else {
        countNumBeth += 0.5;
        countBeth.innerHTML = countNumBeth;
	}
});

function toggleDatePicker(checkboxId) {
        var checkbox = document.getElementById(checkboxId);
        var datePicker = document.getElementById('date' + checkboxId.charAt(0).toUpperCase() + checkboxId.slice(1));

        if (checkbox.checked) {
            datePicker.style.display = 'block';
        } else {
            datePicker.style.display = 'none';
        }
    }







const regionInput = document.getElementById("region");
let locationInput = document.getElementById("location");
const subdistrictInput = document.getElementById("subdistrict");
const streetAddressInput = document.getElementById("streetAddress");

const mapIframe = document.getElementById("map");

regionInput.addEventListener("input", updateMapUrl);
regionInput.addEventListener("input", locationChange);
locationInput.addEventListener("input", updateMapUrl);
subdistrictInput.addEventListener("input", updateMapUrl);
streetAddressInput.addEventListener("input", updateMapUrl);

function updateMapUrl() {
  const region = regionInput.value;
  if (region !== "") {document.getElementById('messages-container-region').style.display = 'none';}
  const location = locationInput.value;
  if (location !== "") {document.getElementById('messages-container-location').style.display = 'none';}
  const subdistrict = subdistrictInput.value;
  const streetAddress = streetAddressInput.value;

  const combinedAddress = `${region}, ${location}, ${subdistrict}, ${streetAddress}`;

  const newMapUrl = `https://www.google.com/maps/embed/v1/place?key=AIzaSyBuNKhbP609Fb3jQassP8wqp9xdebMIT7w&q=${encodeURIComponent(combinedAddress)}`;

  mapIframe.src = newMapUrl;
}


function locationChange() {
    locationInput = document.getElementById("location" + regionInput.value);
    document.getElementById('location').style.display = 'none';
    document.getElementById('locationTest').style.display = 'none';
    document.getElementById('locationBangkok').style.display = 'none';
    document.getElementById("location" + regionInput.value).style.display = 'block';
    locationInput.addEventListener("input", updateMapUrl);
}


































function incrementFormNum1step2(event) {
    event.preventDefault();



    function handleImageUpload(event, fileId) {
        var file = event.target.files[0];
        var reader = new FileReader();

        reader.onload = function (e) {
            var imageSrc = e.target.result;
            displayImage(fileId, imageSrc);
            createImageInput();
        };

        reader.readAsDataURL(file);
    }

    function displayImage(fileId, imageSrc) {
        var container = document.createElement('div');
        container.id = fileId;
        container.className = 'image-container pad';

        var image = document.createElement('div');
        image.className = 'image';

        var imgContainer = document.createElement('div');
        imgContainer.className = 'img-container';

        var img = document.createElement('img');
        img.src = imageSrc;

        var deleteButton = document.createElement('button');
        deleteButton.className = 'delete-button';
        deleteButton.innerHTML = 'X';
        deleteButton.addEventListener('click', function () {
            var container = document.getElementById(fileId);
            container.parentNode.removeChild(container);
            var input = document.getElementById('input-' + fileId);
            input.parentNode.removeChild(input);
            var fileButton = document.querySelector('label[for="input-' + fileId + '"]');
            fileButton.style.display = 'none';
        });

        imgContainer.appendChild(img);
        image.appendChild(imgContainer);
        image.appendChild(deleteButton);
        container.appendChild(image);

        document.getElementById('images-container').appendChild(container);
        var fileButton = document.querySelector('label[for="input-' + fileId + '"]');
            fileButton.style.display = 'none';
    }

    function createImageInput() {
        var fileId = 'file-' + Date.now();

        var container = document.createElement('div');
        container.className = 'image-container';

        var fileButton = document.createElement('label');
        fileButton.className = 'file-button btn sp-condos__btn';
        fileButton.innerHTML = 'Add Photo';
        fileButton.setAttribute('for', 'input-' + fileId);

        var input = document.createElement('input');
        input.name = 'choseImagePlan';
        input.type = 'file';
        input.className = 'file';
        input.accept = 'image/png, image/jpeg, image/jpg';
        input.id = 'input-' + fileId;
        input.addEventListener('change', function (event) {
            handleImageUpload(event, fileId);
        });

        fileButton.appendChild(input);
        container.appendChild(fileButton);

        document.getElementById('images-container').appendChild(container);

        var imagesContainer = document.getElementById('images-container');
        var uploadedImages = imagesContainer.getElementsByClassName('image-container');
    }


    createImageInput();


    var formNumInput = document.getElementById('form_num');
    formNumInput.value = parseInt(formNumInput.value) + 1;
    document.getElementById('startId').style.display = 'none';
    document.getElementById('NextId1step2').style.display = 'block';
}

function previewImage(event) {
            var reader = new FileReader();
            reader.onload = function() {
                var imagePreview = document.getElementById('image-preview');
                var image = document.createElement('img');
                image.src = reader.result;
                imagePreview.appendChild(image);
            };
            reader.readAsDataURL(event.target.files[0]);
}


function incrementFormNum2step2(event) {
    event.preventDefault();


    function handleImageUpload(event, fileId) {
        var file = event.target.files[0];
        var reader = new FileReader();

        reader.onload = function (e) {
            var imageSrc = e.target.result;
            displayImage(fileId, imageSrc);
            createImageInput();
        };

        reader.readAsDataURL(file);
    }

    function displayImage(fileId, imageSrc) {
        var container = document.createElement('div');
        container.id = fileId;
        container.className = 'image-container pad';

        var image = document.createElement('div');
        image.className = 'image';

        var imgContainer = document.createElement('div');
        imgContainer.className = 'img-container';

        var img = document.createElement('img');
        img.src = imageSrc;

        var deleteButton = document.createElement('button');
        deleteButton.className = 'delete-button';
        deleteButton.innerHTML = 'X';
        deleteButton.addEventListener('click', function () {
            var container = document.getElementById(fileId);
            container.parentNode.removeChild(container);
            var input = document.getElementById('input-' + fileId);
            input.parentNode.removeChild(input);
            var fileButton = document.querySelector('label[for="input-' + fileId + '"]');
            fileButton.style.display = 'none';
        });

        imgContainer.appendChild(img);
        image.appendChild(imgContainer);
        image.appendChild(deleteButton);
        container.appendChild(image);

        document.getElementById('images-plan-container').appendChild(container);
        var fileButton = document.querySelector('label[for="input-' + fileId + '"]');
            fileButton.style.display = 'none';
    }

    function createImageInput() {
        var fileId = 'file-' + Date.now();

        var container = document.createElement('div');
        container.className = 'image-container';

        var fileButton = document.createElement('label');
        fileButton.className = 'file-button btn sp-condos__btn';
        fileButton.innerHTML = 'Add Photo';
        fileButton.setAttribute('for', 'input-' + fileId);

        var input = document.createElement('input');
        input.name = 'choseImage';
        input.type = 'file';
        input.className = 'file';
        input.accept = 'image/png, image/jpeg, image/jpg';
        input.id = 'input-' + fileId;
        input.addEventListener('change', function (event) {
            handleImageUpload(event, fileId);
        });

        fileButton.appendChild(input);
        container.appendChild(fileButton);

        document.getElementById('images-plan-container').appendChild(container);

        var imagesContainer = document.getElementById('images-plan-container');
        var uploadedImages = imagesContainer.getElementsByClassName('image-container');
    }

    createImageInput();


    var formNumInput = document.getElementById('form_num');
    formNumInput.value = parseInt(formNumInput.value) + 1;
    document.getElementById('NextId1step2').style.display = 'none';
    document.getElementById('NextId2step2').style.display = 'block';
}


function previewImage(event) {
            var reader = new FileReader();
            reader.onload = function() {
                var imagePreview = document.getElementById('image-preview');

                // Удаление предыдущего изображения, если оно уже существует
                while (imagePreview.firstChild) {
                    imagePreview.removeChild(imagePreview.firstChild);
                }

                var image = document.createElement('img');
                image.src = reader.result;
                imagePreview.appendChild(image);
            };
            reader.readAsDataURL(event.target.files[0]);
        }


function incrementFormNum3step2(event) {
    event.preventDefault();

    var formNumInput = document.getElementById('form_num');
    formNumInput.value = parseInt(formNumInput.value) + 1;
    document.getElementById('NextId2step2').style.display = 'none';
    document.getElementById('NextId3step2').style.display = 'block';
}


function incrementFormNum4step2(event) {
    event.preventDefault();

    var formNumInput = document.getElementById('form_num');
    formNumInput.value = parseInt(formNumInput.value) + 1;
    document.getElementById('NextId3step2').style.display = 'none';
    document.getElementById('startId').style.display = 'block';
}

function incrementFormNum5step2(event) {
    event.preventDefault();

    var formNumInput = document.getElementById('form_num');
    formNumInput.value = parseInt(formNumInput.value) + 1;
    document.getElementById('NextId4step2').style.display = 'none';
    document.getElementById('startId').style.display = 'block';
}



function decrementFormNum3step2(event) {
    event.preventDefault();
    var formNumInput = document.getElementById('form_num');
    formNumInput.value = parseInt(formNumInput.value) - 1;
    document.getElementById('NextId2step2').style.display = 'none';
    document.getElementById('NextId1step2').style.display = 'block';
}

function decrementFormNum4step2(event) {
    event.preventDefault();
    var formNumInput = document.getElementById('form_num');
    formNumInput.value = parseInt(formNumInput.value) - 1;
    document.getElementById('NextId3step2').style.display = 'none';
    document.getElementById('NextId2step2').style.display = 'block';
}


















function incrementFormNum1step3(event) {
    event.preventDefault();

    var radioImmediate = document.getElementById('availableImmediately');
    var radioAfterDate = document.getElementById('availableAfterThisDate');
    var rentalDuration = document.getElementById('rentalDuration');

    // Додавання обробників подій на радіо-кнопки
    radioImmediate.addEventListener('change', function() {
        rentalDuration.style.display = 'block';
    });

    radioAfterDate.addEventListener('change', function() {
        rentalDuration.style.display = 'block';
    });


    var formNumInput = document.getElementById('form_num');
    formNumInput.value = parseInt(formNumInput.value) + 1;
    document.getElementById('startId').style.display = 'none';
    document.getElementById('NextId1step3').style.display = 'block';
}



function incrementFormNum2step3(event) {
    event.preventDefault();

    var dateAvailableAfterThisDate = document.getElementById('dateAvailableAfterThisDate').value;
    var availableAfterThisDate = document.querySelector('input[name="available"]:checked');
    var forSale = document.querySelector('input[name="forSale"]:checked');
    var rentalDuration = document.querySelector('input[name="rentalDuration"]:checked');
    var propertyType = document.querySelector('input[name="propertyType"]:checked');


    if (propertyType.value === 'sell' || propertyType.value === 'both') {
        if (!forSale) {
             document.getElementById('messages-container-forSaleAfterThisDate').style.display = 'block';
             return;
        }
        document.getElementById('messages-container-forSaleAfterThisDate').style.display = 'none';

        if (forSale) {
            document.getElementById('div-sales_price').style.display = 'block';
        }

        if (forSale.value === 'forSaleWithRentalTenant') {
            document.getElementById('dateForSaleWithRentalTenant').style.display = 'block';
        }
        document.getElementById('dateForSaleWithRentalTenant').style.display = 'none';

//         if (dateForSaleWithRentalTenant === "" && forSaleWithRentalTenant.value === "forSaleWithRentalTenant") {
//            document.getElementById('messages-container-RentalTenant').style.display = 'block';
//            return;
//        }
//        document.getElementById('messages-container-RentalTenant').style.display = 'none';
    }

    if (propertyType.value === 'rent' || propertyType.value === 'both') {
        if (!availableAfterThisDate) {
             document.getElementById('messages-container-availableAfterThisDate').style.display = 'block';
             return;
        }
        document.getElementById('messages-container-availableAfterThisDate').style.display = 'none';

        if (dateAvailableAfterThisDate === "" && availableAfterThisDate.value === "availableAfterThisDate") {
            document.getElementById('messages-container-dateAvailable').style.display = 'block';
            return;
        }
        document.getElementById('messages-container-dateAvailable').style.display = 'none';

        if (!rentalDuration) {
             document.getElementById('messages-container-rentalDuration').style.display = 'block';
             return;
        }
        document.getElementById('messages-container-rentalDuration').style.display = 'none';

        if (rentalDuration.value === 'month') {
            document.getElementById('div-NextId3step3Year').style.display = 'block';
            document.getElementById('div-NextId3step3Listing3_6Month').style.display = 'block';
            document.getElementById('div-NextId3step3ListingMonth').style.display = 'block';
        }

        if (rentalDuration.value === '3_6Months') {
            document.getElementById('div-NextId3step3Year').style.display = 'block';
            document.getElementById('div-NextId3step3Listing3_6Month').style.display = 'block';
            document.getElementById('div-NextId3step3ListingMonth').style.display = 'none';
        }

        if (rentalDuration.value === 'year') {
            document.getElementById('div-NextId3step3Year').style.display = 'block';
            document.getElementById('div-NextId3step3Listing3_6Month').style.display = 'none';
            document.getElementById('div-NextId3step3ListingMonth').style.display = 'none';
        }
    }



    var formNumInput = document.getElementById('form_num');
    formNumInput.value = parseInt(formNumInput.value) + 1;
    document.getElementById('NextId1step3').style.display = 'none';
    document.getElementById('NextId2step3').style.display = 'block';
}



function incrementFormNum3step3(event) {
    event.preventDefault();

    var NextId3step3Year = document.getElementById('NextId3step3Year').value;
    var NextId3step3Listing3_6Month = document.getElementById('NextId3step3Listing3_6Month').value;
    var NextId3step3ListingMonth = document.getElementById('NextId3step3ListingMonth').value;
    var SalesPrice = document.getElementById('sales_price').value;
    var rentalDuration = document.querySelector('input[name="rentalDuration"]:checked');
    var propertyType = document.querySelector('input[name="propertyType"]:checked');
    console.log(1)
    if (SalesPrice === "" && propertyType.value === "sell" || SalesPrice === "" && propertyType.value === "both") {
         document.getElementById('messages-container-sales_price').style.display = 'block';
         return;
    }
    document.getElementById('messages-container-sales_price').style.display = 'none';
    console.log(2)
    if (NextId3step3Year === "" && propertyType.value === "rent" || NextId3step3Year === "" && propertyType.value === "both") {
         document.getElementById('messages-container-NextId3step3Year').style.display = 'block';
         return;
    }
    document.getElementById('messages-container-NextId3step3Year').style.display = 'none';
    console.log(3)
    if (propertyType.value === "rent" || propertyType.value === "both") {
        if (NextId3step3Listing3_6Month === "" && rentalDuration.value === '3_6Months' || NextId3step3Listing3_6Month === "" && rentalDuration.value === 'month') {
             document.getElementById('messages-container-NextId3step3Listing3_6Month').style.display = 'block';
             return;
        }

        console.log(4)
        if (NextId3step3ListingMonth === "" && rentalDuration.value === 'month') {
             document.getElementById('messages-container-NextId3step3ListingMonth').style.display = 'block';
             return;
        }
    }
    document.getElementById('messages-container-NextId3step3Listing3_6Month').style.display = 'none';
    document.getElementById('messages-container-NextId3step3ListingMonth').style.display = 'none';

    console.log(5)
    var formNumInput = document.getElementById('form_num');
    formNumInput.value = parseInt(formNumInput.value) + 1;
    document.getElementById('NextId2step3').style.display = 'none';
    document.getElementById('NextId3step3').style.display = 'block';
}


document.addEventListener('DOMContentLoaded', function() {
    var key_1 = document.getElementById('key_1');
    var key_2 = document.getElementById('key_2');
    var key_5 = document.getElementById('key_5');

    var keys_1 = document.getElementById('keys_1');
    var keys_2 = document.getElementById('keys_2');
    var keys_3 = document.getElementById('keys_3');
    var keys_4 = document.getElementById('keys_4');
    var keys_5 = document.getElementById('keys_5');

    keys_1.addEventListener('change', function() {
        key_1.style.display = 'block';
        key_2.style.display = 'none';
        key_5.style.display = 'none';
    });

    keys_2.addEventListener('change', function() {
        key_1.style.display = 'none';
        key_2.style.display = 'block';
        key_5.style.display = 'none';
    });

    keys_3.addEventListener('change', function() {
        key_1.style.display = 'none';
        key_2.style.display = 'none';
        key_5.style.display = 'none';
    });

    keys_4.addEventListener('change', function() {
        key_1.style.display = 'none';
        key_2.style.display = 'none';
        key_5.style.display = 'none';
    });

    keys_5.addEventListener('change', function() {
        key_1.style.display = 'none';
        key_2.style.display = 'none';
        key_5.style.display = 'block';
    });
});

function incrementFormNum4step3(event) {
    event.preventDefault();

    var keys = document.querySelector('input[name="keys"]:checked');

    if(!keys) {
        document.getElementById('messages-container-keys').style.display = 'block';
        return;
    }
    document.getElementById('messages-container-keys').style.display = 'none';


    var formNumInput = document.getElementById('form_num');
    formNumInput.value = parseInt(formNumInput.value) + 1;
    document.getElementById('NextId3step3').style.display = 'none';
    document.getElementById('startId').style.display = 'block';
}



function decrementFormNum2step3(event) {
    event.preventDefault();

    var formNumInput = document.getElementById('form_num');
    formNumInput.value = parseInt(formNumInput.value) - 1;
    document.getElementById('NextId2step3').style.display = 'none';
    document.getElementById('NextId1step3').style.display = 'block';
}

function decrementFormNum3step3(event) {
    event.preventDefault();

    var formNumInput = document.getElementById('form_num');
    formNumInput.value = parseInt(formNumInput.value) - 1;
    document.getElementById('NextId3step3').style.display = 'none';
    document.getElementById('NextId2step3').style.display = 'block';
}


function showDialog(event) {
    event.preventDefault(); // Зупиняє стандартну поведінку кнопки

    var dialogWrapper = document.getElementById('dialog-wrapper');
    dialogWrapper.style.display = 'block';
}


function showWarningMain(event) {
    event.preventDefault(); // Зупиняє стандартну поведінку кнопки

    var phone = document.getElementById('phone').value;
    var i_am = document.getElementById('i_am').value;

    if (phone === '') {
        document.getElementById('messages-container-phone').style.display = 'block';
        return;
    }
    document.getElementById('messages-container-phone').style.display = 'none';

    if (i_am === '') {
        document.getElementById('messages-container-i_am').style.display = 'block';
        return;
    }
    document.getElementById('messages-container-i_am').style.display = 'none';

    var form = document.getElementById("myForm");
    form.submit();
}






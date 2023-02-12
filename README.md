# README

<div align="center">

  [![Contributors][contributors-shield]][contributors-url]
  [![Forks][forks-shield]][forks-url]
  [![Issues][issues-shield]][issues-url]

  <a href="https://github.com/Apres-Ski">
    <img src="https://media.giphy.com/media/xEBZR96wLedVHzOeqw/giphy.gif">
  </a>
  <h2 align="center">Après-Ski</h2>

  <h3 align="center">
    <a href="https://github.com/Apres-Ski/Apres_Ski_BE/issues">Report Bug</a>
    ·
    <a href="https://github.com/Apres-Ski/Apres_Ski_BE/issues">Request Feature</a>
  </h3>
</div>
<br>

Hungry and tired after a day at Breckenridge? Looking to find somewhere that's: fun, good vibes, close enough to walk?

**Find it with Après-Ski!**

The web application geared towards snowsport entheusiests looking to find their post slopes *food & drinks* to round out a good day.
<br>

---

<details>
  <summary>Table of Contents</summary>

  :skier: [MVP](#mvp)
  <br>
  :skier: [Learning Goals](#learning-goals)
  <br>
  :skier: [Project Overview](#project-overview)
  <br>
  :skier: [Planning](#planning)
  <br>
  :skier: [Tech Stack](#tech-stack)
  <br>
  :skier: [Contributors](#contributors)
  <br>

</details>

 <br>

## Getting Started

### Web Usage [Work In Progress]

This is a Django REST Framework API designed for a React web application. To get started, follow the link below and select one of our test-users. Once you selected a user you will be able to:

* Search for restaurants by proximity to the user.
* [get with FE to finish feature list]

<br>

### Local Installation

This back-end application was made with the following:

* Python 3.11.1
* Django 4.1.6

To install and run on your personal computer you will need to do the following:

1. Get a free API Key for Geoapify's Routing-API at [Geoapify](https://www.geoapify.com/).

2. Fork and clone the repo to your local machine.

3. In the root directory of APRES_SKI_BE, create a file named `keys.py`.

4. Inside `keys.py` create a variable named `routing_key = 'your_key_as_string'`

    * Note: `keys.py` should be *grayed out*. If it is not, check the `.gitignore` and resolve the issue before pushing any changes.

5. Install requirements.

    ```zsh
    pip3 install -r requirements.txt
    ```

6. Start a server.

    ```zsh
    python3 manage.py runserver
    ```

7. Navigate to <http://localhost:8000/api/v1/>

<br />

## API Endpoints
### GET

<details>
<summary> <code>localhost:8000/api/v1/restaurants</code> </summary>

### GET /api/v1/restaurants

> Get a list of recipes from a random country (if no params are passed) OR by selected country, through params.

**Parameters**

> | Name | Required | Type | Description |

> | -------------:|:--------:|:-------:| ---------------- |

> | `country` | no | string | The country you want to get recipes from. |

**Response**

> ```
> {
> "data": [
> {
> "id": null,
> "type": "recipe",
> "attributes": {
> "title": "Andy Ricker's Naam Cheuam Naam Taan Piip (Palm Sugar Simple Syrup)",
> "url": "https://www.seriouseats.com/recipes/2013/11/andy-rickers-naam-cheuam-naam-taan-piip-palm-sugar-simple-syrup.html",
> "country": "Thailand",
> "image": "https://edamam-product-images.s3.amazonaws.com..."
> }
> },
> {
> "id": null,
> "type": "recipe",
> "attributes": {
> "title": "Sriracha",
> "url": "http://www.jamieoliver.com/recipes/vegetables-recipes/sriracha/",
> "country": "Thailand",
> "image": "https://edamam-product-images.s3.amazonaws.com/."
> }
> },
> {...},
> {...},
> {...},
> {etc},
> ]
> }
> ```

</details>






<br>

## Project Overview
### Planning

<br>

### MVP

<br>

### Learning Goals

<br>

### Tech Stack

<br>

## Contributors

<table>
  <tr>
    <th>Joseph Hilby</th>
    <th>Tricia Holmes</th>
    <th>Ryan Nagel</th>
    <th>Kristen Nestler</th>
    <th>Kevin Ta</th>
    <th>Matt Walter</th>
  </tr>
  <tr>
    <td><img style="max-width:300px;width:100%" src="https://media.licdn.com/dms/image/C4E03AQEdZUKFgryaqg/profile-displayphoto-shrink_800_800/0/1567961066772?e=1680739200&v=beta&t=TFQt8RiDDMpJHbytApiShBpLVCCZlfeuUwLffp95tG8"></td>
    <td><img style="max-width:300px;width:100%" src="https://media.licdn.com/dms/image/D4E03AQF88CLqrqQ1uA/profile-displayphoto-shrink_800_800/0/1663436465329?e=1680739200&v=beta&t=2cbhih9hldc3dkTuiAK5uBr0ZsaVKiTwM4349AAAd-o"></td>
    <td><img style="max-width:300px;width:100%" src="https://avatars.githubusercontent.com/u/108195380?v=4"></td>
    <td><img style="max-width:300px;width:100%" src="https://media.licdn.com/dms/image/D4E03AQESEnUYGJprLA/profile-displayphoto-shrink_800_800/0/1673023729512?e=1680739200&v=beta&t=PhhX0_wEMPxiu2nO-OfDyCv73Ro_iyyGPjQ4YUnXSC4"></td>
    <td><img style="max-width:300px;width:100%" src="https://avatars.githubusercontent.com/u/36166420?v=4"></td>
    <td><img style="max-width:300px;width:100%" src="https://avatars.githubusercontent.com/u/106847513?v=4"></td>
  </tr>

  <tr>
    <td>
       <a href="https://github.com/josephhilby" rel="nofollow noreferrer">
          <img src="https://i.stack.imgur.com/tskMh.png" alt="github"> Github
      </a><br>
        <a href="https://www.linkedin.com/in/josephmhilby" rel="nofollow noreferrer">
          <img src="https://i.stack.imgur.com/gVE0j.png" alt="linkedin"> LinkedIn
      </a>
    </td>
    <td>
      <a href="https://github.com/tricia-holmes"  rel="nofollow noreferrer">
          <img src="https://i.stack.imgur.com/tskMh.png" alt="github"> Github
        </a><br>
      <a href="https://www.linkedin.com/in/triciaholmes/" rel="nofollow noreferrer">
    <img src="https://i.stack.imgur.com/gVE0j.png" alt="linkedin"> LinkedIn
        </a>
    </td>
    <td>
      <a href="https://github.com/Nagel29"  rel="nofollow noreferrer">
          <img src="https://i.stack.imgur.com/tskMh.png" alt="github"> Github
        </a><br>
      <a href="https://www.linkedin.com/in/ryan-nagel-000280173/" rel="nofollow noreferrer">
    <img src="https://i.stack.imgur.com/gVE0j.png" alt="linkedin"> LinkedIn
        </a>
    </td>
    <td>
      <a href="https://github.com/knestler" rel="nofollow noreferrer">
          <img src="https://i.stack.imgur.com/tskMh.png" alt="github"> Github
        </a><br>
      <a href="https://www.linkedin.com/in/kristen-nestler/" rel="nofollow noreferrer">
    <img src="https://i.stack.imgur.com/gVE0j.png" alt="linkedin"> LinkedIn
        </a>
    </td>
    <td>
      <a href="https://www.linkedin.com/in/kevin-ta-b1a36723b/" rel="nofollow noreferrer">
          <img src="https://i.stack.imgur.com/tskMh.png" alt="github"> Github
        </a><br>
      <a href="https://github.com/KevinT001" rel="nofollow noreferrer">
    <img src="https://i.stack.imgur.com/gVE0j.png" alt="linkedin"> LinkedIn
        </a>
    </td>
    <td>
      <a href="https://github.com/MattWalterTX" rel="nofollow noreferrer">
          <img src="https://i.stack.imgur.com/tskMh.png" alt="github"> Github
            </a><br>
            <a href="https://www.linkedin.com/in/matt-walter-67b810246/" rel="nofollow noreferrer">
    <img src="https://i.stack.imgur.com/gVE0j.png" alt="linkedin"> LinkedIn
        </a><br>
    </td>
  </tr>
</table>

## Contributing

Do you have a better & cooler way of doing what I did? Your contribution would be **greatly appreciated**.

Please fork the repo, create your branch, and create a pull request. You can also simply open an issue with the tag "enhancement".

1. Fork the Project

2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)

3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)

4. Push to the Branch (`git push origin feature/AmazingFeature`)

5. Open a Pull Request

Thanks again!


## Acknowledgments

* Turing School of Software Design: [https://turing.edu/](https://turing.edu/)

* DBdiagram.io: [https://dbdiagram.io/home](https://dbdiagram.io/home)

* Best-README-Template: [https://github.com/othneildrew/Best-README-Template](https://github.com/othneildrew/Best-README-Template)

* API-endpoints: [https://github.com/bufferapp/README/blob/master/billing/api-endpoints.md](https://github.com/bufferapp/README/blob/master/billing/api-endpoints.md)


<!-- MARKDOWN LINKS & IMAGES -->

<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/josephhilby/lunch_and_learn.svg?style=for-the-badge

[contributors-url]: https://github.com/Apres-Ski/Apres_Ski_BE/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/Apres-Ski/Apres_Ski_BE.svg?style=for-the-badge

[forks-url]: https://github.com/othneildrew/Apres-Ski/Apres_Ski_BE/network/members

[issues-shield]: https://img.shields.io/github/issues/Apres-Ski/Apres_Ski_BE.svg?style=for-the-badge

[issues-url]: https://github.com/Apres-Ski/Apres_Ski_BE/issues

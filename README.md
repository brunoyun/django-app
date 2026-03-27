# Impact for Gradual Semantics

This repository contains a Django web application for computing argument strengths and impact in Dung-style argumentation graphs described with ASPARTIX syntax.

The app lets you:

1. Parse and visualize an argumentation graph.
2. Compute argument degrees with several gradual semantics.
3. Compute attack intensities (Shapley-inspired contribution values).
4. Compute the impact of a set of source arguments X on a target argument x.

## Demo

Live demo: [https://impact-gradual-semantics.vercel.app/](https://impact-gradual-semantics.vercel.app/)

![Application interface](https://bruno-yun.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F57e14b1b-ce77-483b-a9ed-537a76c86282%2F594f0392-5dbc-4463-bd53-419656ec7ed3%2FCapture_decran_2023-10-12_a_13.07.14.png?table=block&id=45d27bc7-5e0b-44a8-aa9c-716f5fb22af0&spaceId=57e14b1b-ce77-483b-a9ed-537a76c86282&width=1420&userId=&cache=v2)

## Project Structure

- `vercel_app/`: Django project settings and root URL config.
- `MyApp/`: core app (views, URL routing, templates, semantics and impact logic).
- `MyApp/templates/MyApp/index.html`: single-page UI with AJAX calls.
- `vercel.json`: Vercel serverless deployment configuration.

## ASPARTIX Input Format

The app accepts Dung argumentation frameworks in ASPARTIX format:

```text
arg(a1).
arg(a2).
att(a1,a2).
```

This defines two arguments (`a1`, `a2`) and one attack from `a1` to `a2`.

Reference: [TU Wien - Dung argumentation systems](https://www.dbai.tuwien.ac.at/proj/argumentation/systempage/dung.html)

## Implemented Semantics

### Gradual semantics

- H-categoriser semantics (`cat`)
- Cardinality-based semantics (`card`)
- Max-based semantics (`max`)
- Counting semantics (`cs`)

### Impact semantics

- Shapley-based impact semantics
- Delobelle and Villata impact semantics

## Local Development

### 1. Prerequisites

- Python 3.10+ (3.11 recommended)
- pip

### 2. Install dependencies

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Run the app

```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## How to Use

1. Enter ASPARTIX text in the input area.
2. Select one gradual semantics.
3. Click Compute.
4. Inspect:
   - parser logs in the console,
   - graph rendering,
   - argument degree table,
   - attack contribution labels.
5. (Optional) In the Impact section:
   - choose a source set X,
   - choose a target x,
   - choose impact semantics,
   - click Compute Impact.

## HTTP Endpoints

- `GET /`: render the UI.
- `POST /compute_graph/`: parse graph + compute degrees + attack intensities.
- `POST /compute_impact/`: compute impact value using current graph and selected semantics.

## Deployment (Vercel)

This project is configured for Vercel Python serverless deployment through `vercel_app/wsgi.py`.

Typical deployment flow:

```bash
npm i -g vercel
vercel
```

The included `vercel.json` routes all requests to the Django WSGI entrypoint.

## References

- [Amgoud et al. 2017 - Acceptability Semantics for Weighted Argumentation Frameworks](https://www.ijcai.org/proceedings/2017/0009.pdf)
- [Amgoud et al. 2022 - Evaluation of argument strength in attack graphs: Foundations and semantics](https://www.sciencedirect.com/science/article/abs/pii/S0004370221001582)
- [Borg and Floris 2021 - A basic framework for explanations in argumentation](https://ieeexplore.ieee.org/document/9329042)
- [Amgoud et al. 2017 - IJCAI Proceedings](https://www.ijcai.org/Proceedings/2017/10)

## Citation

If you use this work in your research, please cite:

```bibtex
@article{DBLP:journals/corr/abs-2407-08302,
  author       = {Caren Al Anaissy and
                  J{\'{e}}r{\^{o}}me Delobelle and
                  Srdjan Vesic and
                  Bruno Yun},
  title        = {Impact Measures for Gradual Argumentation Semantics},
  journal      = {CoRR},
  volume       = {abs/2407.08302},
  year         = {2024},
  url          = {https://doi.org/10.48550/arXiv.2407.08302},
  doi          = {10.48550/ARXIV.2407.08302},
  eprinttype   = {arXiv},
  eprint       = {2407.08302},
  timestamp    = {Fri, 16 Aug 2024 14:50:28 +0200},
  biburl       = {https://dblp.org/rec/journals/corr/abs-2407-08302.bib},
  bibsource    = {dblp computer science bibliography, https://dblp.org}
}
```

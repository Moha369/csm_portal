# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

- CSS Tweaks to bring the `post_detail.html` page into the modern era
- Table tweaks for JIRA data

## [0.0.3] - 2019-09-02
### Added

- JIRA and Pendo API data is now being populated after using `render_to_response` function within the class `PostDetailView`

## [0.0.2] - 2019-07-17
### Added

- Google SSO using `social-django`
- login / logout user views and functions
- mappings to relevant dashboards using `.btn`
- table layout added to `post_detail.html` to display JIRA ticket data

## [0.0.1] - 2019-07-16

- Initial Commit

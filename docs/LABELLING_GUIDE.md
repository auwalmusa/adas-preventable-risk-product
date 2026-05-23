# Labelling Guide

## Purpose

This guide standardises how crash videos are converted into labelled analytical records. It is designed to make the dataset consistent, auditable, and realistic for a Senior Data Analyst technical presentation.

## Unit of Analysis

The unit of analysis is a crash incident, not necessarily a whole YouTube video.

- A short single-incident clip usually creates one row.
- A long compilation video can create many rows.
- Each labelled incident must have its own `crash_timestamp_start`.

## Inclusion Criteria

Include an incident when:

- at least one impact is clearly visible
- the sequence allows a reasonable judgement of secondary impacts
- the footage is clear enough to assess weather, road type, and likely human factors

Prioritise:

- chain-reaction motorway or highway crashes
- pile-ups in rain, fog, snow, or ice
- rear-end secondary impacts
- incidents where AEB, FCW, or ACC relevance is plausible

## Exclusion Criteria

Exclude or mark for review when:

- the actual impact is off-screen
- there is no clear crash sequence
- the clip is commentary-only or not road-crash footage
- the video is a tutorial, news summary without usable footage, or unrelated content
- the timestamp cannot be identified

## Timestamping

Use the timestamp where the crash sequence begins, not where the video starts.

Examples:

- `0:17`
- `1:45`
- `12:08`

For compilation videos, use the start of the specific incident.

## Initial Impact Unavoidable

Use `Yes` when the first impact was plausibly unavoidable for a typical attentive driver, such as:

- less than 2 seconds warning
- sudden black ice
- sudden dense fog
- mechanical failure
- another vehicle abruptly entering the path with no realistic escape

Use `No` when the first impact appears avoidable through ordinary safe driving, such as:

- excessive speed
- following too close
- clear red-light violation
- visible hazard with adequate warning time

Use `notes` for borderline cases.

## Secondary Preventable by ADAS

Use `Yes` when current ADAS could realistically prevent most secondary impacts in the sequence.

Use `Partial` when ADAS could reduce severity or prevent some, but not all, secondary impacts.

Use `No` when:

- impacts happen too quickly for intervention
- the secondary impact is side/rear impact outside likely ADAS capability
- road conditions make prevention unrealistic
- the available footage does not support the claim

## ADAS Feature Labels

Common values:

- `AEB`
- `FCW`
- `ACC`
- `AEB + FCW`
- `AEB + FCW + ACC`

Only include features that are plausibly relevant to the observed crash sequence.

## Severity Labels

Use:

- `Minor`: low-speed contact, limited visible damage
- `Moderate`: meaningful impact, visible damage, likely insurance claim
- `Severe`: high-energy impact, pile-up, rollover, major vehicle damage
- `Fatal`: only when stated by credible source or clearly documented

Do not infer fatality from visual severity alone.

## Notes

Use `notes` to capture:

- uncertainty
- unusual weather or road conditions
- why ADAS was or was not plausible
- whether the row needs review

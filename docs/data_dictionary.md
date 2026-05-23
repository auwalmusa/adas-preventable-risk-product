# Data Dictionary - ADAS Preventable Risk Product

## Core Schema

| Column                         | Type     | Description                                      | Allowed Values                        |
| ------------------------------ | -------- | ------------------------------------------------ | ------------------------------------- |
| date_watched                   | Date     | Date the video was labelled                      | YYYY-MM-DD                            |
| video_id                       | Text     | Unique YouTube video ID                          | yt_xxxxxxx                            |
| video_title                    | Text     | Title of the YouTube video                       | -                                     |
| video_url                      | Text     | Full YouTube URL                                 | -                                     |
| country                        | Category | Country where crash occurred                     | UK, USA, Russia, Canada, Australia... |
| weather                        | Category | Weather conditions                               | Clear, Rain, Snow, Fog, Ice, Night    |
| road_type                      | Category | Type of road                                     | Motorway, Urban, Rural, Junction      |
| crash_timestamp_start          | Text     | Timestamp in video where crash begins            | e.g. 2:15                             |
| initial_impact_unavoidable     | Boolean  | Was the first impact unavoidable?                | Yes / No                              |
| reason_unavoidable             | Text     | Reason why first impact was unavoidable          | Free text                             |
| num_total_impacts              | Integer  | Total number of impacts in the chain             | 1,2,3...                              |
| num_secondary_impacts          | Integer  | Number of impacts after the first one            | 0,1,2...                              |
| secondary_preventable_by_adas  | Category | Could ADAS have prevented the secondary impacts? | Yes, Partial, No                      |
| adas_features_needed           | Text     | Which ADAS features would have helped            | AEB, FCW, ACC, etc.                   |
| main_human_error_in_secondary  | Category | Main human factor in secondary crashes           | Following too close, Distracted, etc. |
| estimated_severity             | Category | Estimated severity of the crash                  | Minor, Moderate, Severe, Fatal        |
| notes                          | Text     | Any additional observations                      | -                                     |

## Decision Rules

- `initial_impact_unavoidable` = `Yes` if there was less than 2 seconds warning, such as black ice, sudden fog, or mechanical failure.
- `secondary_preventable_by_adas` = `Yes` if ADAS could realistically stop the second or third impact.

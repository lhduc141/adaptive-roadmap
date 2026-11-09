# PROJECTS, GOALS & PROGRESS
> **Mục đích của file**
> File này chứa những thông tin thay đổi thường xuyên hơn:
> - Các project tôi đã và đang xây dựng.
> - Những quyết định kỹ thuật tôi từng đưa ra.
> - Kinh nghiệm thực tế.
> - Mục tiêu nghề nghiệp.
> - Roadmap.
> - Skill gaps hiện tại.
> - Progress log.
> - Portfolio.
> File này giúp AI hiểu không chỉ **tôi biết gì**, mà còn **tôi đã thực sự làm gì và đang muốn đi đâu**.

---

## Project Index có thể thêm

| Project                                                       | Loại                                     | Vai trò                                                                        | Tech Stack                                                                     | Trạng thái                              | Mức quan trọng |
| ------------------------------------------------------------- | ---------------------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | --------------------------------------- | -------------- |
| EVNHCMC CRM                                                   | Enterprise / Production Team             | Frontend Developer — Ticket Workflow Owner / Cross-stack Debugging Contributor | ReactJS, TypeScript, Redux Toolkit, RTK Query, Socket.IO, Ant Design, Tailwind | Production / Contribution Ended         | High           |
| LinguaPanda                                                   | Bachelor Thesis / Solo Project           | Solo Full-stack Developer / System Designer / Thesis Researcher                | Next.js, NestJS, PostgreSQL, Prisma, Redis, BullMQ, Groq, Azure Speech, Docker | Deployed MVP / Thesis Completed         | High           |
| AI-Based Automatic Student Attendance Device for School Buses | Scientific Research / Team               | Core Research Member / Flutter Developer / UI/UX & Requirements Contributor    | Flutter, Dart, Google ML Kit, REST API, Camera, Figma                          | Research Prototype / Functional Demo    | High           |
| eSign                                                         | EVNHCMC Internal Business Application    | Full-stack Developer / Main Developer                                          | Next.js, NestJS, SQL Server, Sequelize, LDAP, JWT, Docxtemplater, Docker       | Internal Development / Testing          | Medium         |
| e-Retire                                                      | EVNHCMC Internal Business Application    | Full-stack Developer / Main Developer                                          | Next.js, NestJS, PostgreSQL, Prisma, JWT, HRMS Integration                     | Completed Development / Pending Rollout | Medium         |
| Manach                                                        | University / Team — Software Engineering | Frontend Lead / Integration & Testing Contributor                              | ReactJS, Vite, Redux Toolkit, Tailwind, DaisyUI, Ant Design, Chart.js          | Completed / Archived                    | Medium         |
| Farming Assistance                                            | University / Team — Database Project     | Frontend Lead / UI Designer / Database Design Contributor                      | ReactJS, Redux Toolkit, Tailwind, ExpressJS, Sequelize, MySQL                  | Completed / Archived                    | Medium         |
| BC64 Capstone Movie                                           | Cybersoft Practical Training / Team      | Frontend Developer                                                             | ReactJS, Redux Toolkit, Axios, Tailwind, Ant Design                            | Completed / Archived                    | Low            |
| V-Learning                                                    | Cybersoft Practical Training / Team      | Frontend Developer                                                             | ReactJS, Redux Toolkit, Axios, Tailwind, MUI, Ant Design                       | Completed / Archived                    | Low            |
| NeoPac Ninja                                                  | Team / Learning Project                  | JavaScript Game Developer / Core Gameplay Contributor                          | JavaScript, HTML Canvas, HTML, CSS                                             | Completed / Archived                    | Low            |
| TCR Netcentric                                                | University / Team                        | Go Developer / TCP Server & Game Logic Developer                               | Go, TCP, JSON                                                                  | Completed / Archived                    | Low            |


# PROJECT — EVNHCMC CRM

## Overview

**Tên project:** EVNHCMC CRM — Customer Care Ticket Processing & Omni-channel Operations Platform  
**Thời gian tham gia:** 11/2024 → 03/2026  
**Trạng thái:** Production — UAT & PROD  
**Loại project:** Enterprise / Internal Production System — EVNHCMC Customer Care Center  
**Vai trò của tôi:** Frontend Developer — primary owner of the local electricity-unit ticket-processing frontend; Shift Supervisor UI Contributor; Cross-stack Debugging & Integration Contributor  
**Portfolio priority:** Flagship / Primary Real-world Production Project

EVNHCMC CRM là hệ thống chăm sóc khách hàng và vận hành nghiệp vụ được sử dụng thực tế trong hệ sinh thái Tổng công ty Điện lực TP.HCM. Hệ thống bao phủ nhiều domain như customer care, call/chat/omni-channel, ticket/request processing, organization assignment, agent operation, supervisor monitoring, reporting, administration và tích hợp với các hệ thống EVN khác.

Đây là codebase lớn do nhiều team cùng phát triển. Tôi **không claim ownership toàn bộ CRM hoặc backend architecture**. Phần tôi chịu trách nhiệm chính là **toàn bộ frontend workflow xử lý phiếu yêu cầu tại các Điện lực địa phương**, từ phân tích business flow và UI/state đến implementation, performance optimization, UAT và production support. Tôi cũng phát triển thêm một phần giao diện dành cho **trưởng ca**.

CRM là project production quan trọng nhất trong kinh nghiệm làm việc tại EVNHCMC vì đây là nơi tôi làm việc trực tiếp với workflow thật, user thật, tải hệ thống thật, codebase nhiều developer và quy trình release UAT/PROD.

## Business Context & Scope

CRM phục vụ quá trình tiếp nhận và xử lý các yêu cầu chăm sóc khách hàng điện lực.

Ở mức tổng thể, một interaction có thể đi qua:

```
Customer
→ Call / Chat / Website / App / Other Channel
→ Customer Care Session
→ Customer Lookup / Identification
→ Create Request / Ticket
→ Route to Responsible Unit
→ Reception
→ Processing
→ Collaboration / Transfer if required
→ Completion
→ History / Reporting / Customer Feedback
```

Hệ thống được sử dụng bởi nhiều nhóm người dùng:

- Điện thoại viên / customer-care agents.
    
- Nhân viên xử lý yêu cầu tại các Điện lực địa phương.
    
- Trưởng ca / supervisor.
    
- Nhân viên và manager tại các đơn vị liên quan.
    
- Administrator và các nhóm vận hành hệ thống.
    

Phần workflow tôi phụ trách tập trung vào **quy trình phiếu tại đơn vị điện lực địa phương**. Đây là production workflow được sử dụng thường xuyên để xử lý yêu cầu khách hàng thật trên phạm vi các Điện lực thuộc EVNHCMC.

## Core Ticket Workflow I Owned

Frontend workflow chính được tổ chức theo các trạng thái nghiệp vụ như:

```
Chờ tiếp nhận
→ Đang xử lý
→ Hoàn thành
```

Ngoài flow cơ bản, source còn có các trạng thái/nhánh như:

```
Phối hợp xử lý
Trở ngại
Chuyển đơn vị
Chuyển team / phòng
Chuyển trung tâm
CMIS-related processing
Cancelled / transferred states
```

Trong frontend hiện tại, các tab chính của request workflow gồm:

```
pending_reception
in_progress
collaboration
completed
obstacle
```

Tôi phụ trách frontend end-to-end của quy trình này, bao gồm:

- Danh sách phiếu theo trạng thái.
    
- Filter/search.
    
- Pagination.
    
- Badge/count theo từng trạng thái.
    
- Xem chi tiết phiếu.
    
- Tiếp nhận phiếu.
    
- Xử lý phiếu.
    
- Phối hợp xử lý.
    
- Chuyển đơn vị/team/phòng khi nghiệp vụ yêu cầu.
    
- Xử lý trở ngại.
    
- Hoàn thành phiếu.
    
- Batch actions ở các luồng được hỗ trợ.
    
- Hiển thị lịch sử và thông tin liên quan.
    
- Đồng bộ thay đổi trạng thái theo real-time event.
    
- Giữ context/filter/paging khi người dùng chuyển tab.
    
- Xử lý UI state khi danh sách thay đổi do người dùng khác thao tác.
    

Tôi không chỉ nhận UI đã hoàn chỉnh rồi code. Tôi có tham gia **phân tích requirement/business flow và đề xuất cách tổ chức UI/state** cho quy trình trước khi implementation.

## System-wide CRM Features

Ngoài khu vực tôi trực tiếp phụ trách, CRM codebase tổng thể có nhiều module khác mà tôi từng phải hiểu để tích hợp/debug:

### Customer Care

- Customer lookup.
    
- Customer detail.
    
- Customer support sessions.
    
- Electricity/customer information.
    
- Contact histories.
    
- Customer request histories.
    
- VIP/customer grouping related flows.
    

### Omni-channel

- Call sessions.
    
- Chat sessions.
    
- Agent status.
    
- Call/chat histories.
    
- Socket-based real-time events.
    
- Social/other channel integration.
    
- Callbot/chatbot/AI-agent related modules.
    

### Ticket Operations

- Ticket creation.
    
- Ticket reception.
    
- Processing.
    
- Collaboration.
    
- Transfers.
    
- Deadlines.
    
- Ticket events/history.
    
- Complaint/feedback.
    
- Additional information.
    
- File attachments.
    
- Ticket templates.
    
- Excel import/export related workflows.
    

### Operations & Supervisor

- Agent map.
    
- Shift.
    
- Working schedule.
    
- Supervisor monitoring.
    
- Agent status.
    
- Organization/team assignment.
    

### Administration

- Users.
    
- Roles.
    
- Permissions.
    
- Organizations.
    
- User groups.
    
- Channels.
    
- Service types.
    
- System configuration.
    
- FAQ/instructions.
    
- Other operational master data.
    

These modules are **system context**, not a claim that I personally implemented all of them.

## Tech Stack

### Frontend

- React 18
    
- TypeScript
    
- React Router
    
- Redux Toolkit
    
- RTK Query
    
- Axios
    
- Ant Design
    
- Tailwind CSS
    
- Socket.IO Client
    
- TinyMCE
    
- Chart.js
    
- React Window
    
- Intersection Observer
    
- localStorage / sessionStorage for selected client-side state and caching
    

### Backend — Team-owned System Context

- NestJS 10
    
- TypeScript
    
- Sequelize / sequelize-typescript
    
- Microsoft SQL Server
    
- MongoDB / Mongoose for selected document/message domains
    
- Redis
    
- RabbitMQ
    
- Kafka
    
- Elasticsearch
    
- MinIO
    
- LDAP / Active Directory
    
- JWT
    
- Socket.IO / WebSocket gateways
    
- Swagger
    
- Docker
    
- GitLab CI/CD
    

I did not own the CRM backend implementation, but I regularly read backend controllers/services/models and API flows when debugging frontend/integration issues.

## Architecture

CRM backend is a multi-application NestJS ecosystem rather than a single server.

Main applications visible in the archived source include:

```
api-gateway
auth-service
chat-service
contacts-service
notification-service
omni-channel-service

ws-chat
ws-notification
ws-omni-channel
```

Shared infrastructure libraries include:

```
RabbitMQ
Redis
Kafka
JWT
LDAP
MinIO
HTTP
Excel
Mail
Shared DTO / Utilities
```

A simplified system view:

```
                        React CRM Portal
                       /                \
                  REST API            Socket.IO
                     ↓                    ↓
              NestJS API Gateway     WS Gateways
                     │                    │
        ┌────────────┼────────────┐       │
        ↓            ↓            ↓       ↓
    SQL Server     Redis      RabbitMQ / Services
        │
        ├─ Elasticsearch
        ├─ MongoDB
        ├─ MinIO
        ├─ Kafka
        └─ External EVN Systems
```

This architecture is owned by the CRM engineering team. My responsibility was to understand enough of these boundaries to build and troubleshoot the frontend correctly rather than treating the backend as a black box.

## Data & Workflow Model

Ticket processing is richer than a single `ticket.status`.

Source models show concepts such as:

```
Ticket
├─ Ticket Event
├─ Ticket Distribution
├─ Ticket Deadline
├─ Additional Information
├─ Complaint / Feedback
├─ Files
├─ Customer Information
└─ Related Processing Data
```

### Ticket Distribution

Distribution records represent assignment/transfer relationships such as:

```
From Organization / Team
→ To Organization / Team
→ Assignee
→ Primary / Collaborative Processing
→ Assignment Time
→ Current Active State
```

### Ticket Event / History

Event/history data records changes through the workflow:

```
Previous State
→ Action
→ Current State
→ Organization / User / Shift
→ Timestamp
```

This is why frontend ticket handling behaves more like a domain-specific workflow application than a simple CRUD screen.

## Authentication & Authorization — System Context

CRM supports internal authentication flows including local CRM identity and LDAP/Active Directory-related login.

At system level:

```
Login
→ Authentication
→ JWT Access / Refresh
→ Redis-backed token/session state
→ Organization / User Context
→ Permission-based Authorization
```

Authorization is fine-grained rather than only `ADMIN` / `USER`.

Permissions cover operations such as:

- read/create/update ticket
    
- customer lookup
    
- pending/processing/completed ticket operations
    
- ticket transfer
    
- call/chat
    
- report access
    
- user/role/permission management
    
- configuration and administration
    

Login/logout also interacts with operational agent state such as shift/agent/omni-channel status.

I consumed this authorization model from the frontend and used permissions/routes/actions appropriately, but I do not claim ownership of the authentication backend.

## My Contribution

### Frontend Ownership — Local Electricity-unit Ticket Workflow

My largest CRM contribution was owning the frontend flow used by local electricity units to receive and process customer request tickets.

I participated in:

```
Business Requirement
→ Analyze Existing Workflow
→ Discuss / Propose UI & State Flow
→ Implement React UI
→ API Integration
→ Real-time State Handling
→ Performance Optimization
→ Internal Validation
→ UAT
→ Production
→ Production Issue Support
```

This was not a demo workflow. The functionality was deployed to production and used by employees handling real customer requests throughout EVNHCMC's local electricity units.

### Shift Supervisor UI

I also implemented additional UI/features for the **trưởng ca / shift supervisor** role.

This exposed me to a different view of the same operational data: not only processing an individual ticket, but supporting monitoring/coordination responsibilities at supervisory level.

### Requirement & UI-state Analysis

For the local-unit workflow, I participated in business-flow analysis and proposed how frontend state and interactions should behave.

This included reasoning about:

- which ticket state the user is currently viewing;
    
- which actions are valid in each state;
    
- what should happen after reception/processing/transfer/completion;
    
- how tab counts should update;
    
- how another user's action should affect the current user's list;
    
- when data should be refreshed;
    
- when cached data is still valid;
    
- how to avoid making agents repeatedly wait for full reloads.
    

### Cross-stack Debugging

Although I was not the main NestJS backend developer, I did not immediately send every issue to the backend team.

My debugging workflow was commonly:

```
Bug / Incorrect UI Behavior
→ Reproduce
→ Check React State / Request Payload / Network Response
→ Read Relevant Frontend Code
→ Inspect Relevant Backend Controller / Service / Query
→ Identify likely layer/root cause

If FE:
→ Fix myself

If BE:
→ Explain specific suspected backend location/problem
→ Coordinate with backend developer
→ Retest integration
```

This significantly improved my ability to work in a large codebase because I learned to reason across the API boundary rather than treating every server response as someone else's problem.

## Performance Optimization Case

One of the most important production problems I handled was the ticket-list loading strategy.

### Initial Problem

An earlier implementation loaded multiple ticket-status datasets aggressively.

Conceptually:

```
Open Ticket Processing Page
→ Request multiple status lists
→ Users switch/reload tabs
→ Lists are fetched repeatedly
→ High concurrent backend workload
```

During heavy periods, the team observed backend/server utilization around **85–90%**.

The problem was especially important because the CRM is used concurrently by many real users, so a frontend request pattern that looks acceptable for one browser can become expensive when multiplied across the organization.

### Optimization Strategy

I changed the frontend toward a **client-side per-status cache + targeted synchronization** model.

Main ideas:

```
Fetch Ticket Data
→ Cache by Status in Browser
→ Render from Local Cache when possible

User switches tab
→ Use cached list immediately
→ Avoid unnecessary full reload

Backend emits relevant Socket event
→ Determine affected status/tab
→ Refresh only relevant data
→ Compare/update local list
→ Add new items
→ Remove items no longer belonging to that status
→ Update UI
```

The current source reflects this direction with:

- `localStorage` cache per ticket status.
    
- Cached counts.
    
- Cached filters.
    
- Cached pagination.
    
- Reuse of local data when no forced refresh is needed.
    
- Selective invalidation of affected tab caches.
    
- Socket-based refresh.
    
- Targeted count refresh.
    
- Debouncing groups of socket events before refetching the active list.
    
- UI rendering from client-side data instead of forcing a full loading state for every tab transition.
    

The purpose was not to remove server synchronization. The purpose was to stop treating every UI interaction as a reason to re-fetch every list.

### Result

After these optimizations, observed backend/server utilization during the hottest periods was reduced to roughly **65–70%**.

The metric is retained as an operational observation from the team rather than claimed as a formal benchmark or isolated CPU-only measurement.

### Important Trade-off

The optimization shifts complexity from the backend to frontend cache consistency.

Instead of:

```
Server is always queried
→ simpler client
→ expensive repeated requests
```

the system becomes:

```
Server remains source of truth
+
Browser cache improves UX/load
+
Socket events invalidate/update relevant cache
```

Benefits:

- fewer unnecessary API calls;
    
- faster tab switching;
    
- lower perceived loading time;
    
- reduced backend load;
    
- better experience during peak usage.
    

Costs:

- cache invalidation becomes more complex;
    
- stale-data risk must be handled;
    
- socket/event behavior becomes important;
    
- localStorage/server consistency must be considered;
    
- more edge cases appear when another user changes a ticket concurrently.
    

This was one of the most valuable practical performance lessons from the CRM project.

## Real-time Synchronization

Ticket lists cannot behave like static CRUD lists because multiple agents can process data concurrently.

Current frontend architecture uses Socket.IO notifications to determine which ticket status is affected by an event.

The pattern is conceptually:

```
Another User / Backend Action
→ Socket Notification
→ Map Event Type to Affected Status Tabs

Inactive Tab
→ Invalidate Cached Data / Count

Active Tab
→ Debounced Targeted Refetch
→ Update Local Cache
→ Re-render
```

This helps users see that a ticket has moved, appeared or disappeared without repeatedly reloading every status.

The system also handles changes in ticket availability/state caused by other users. I no longer remember the exact name of every temporary business status used for ticket viewing/processing, so the project record intentionally does not invent those names.

## Frontend State & Performance Patterns

The CRM source uses many performance and state-management patterns, including:

- RTK Query.
    
- Redux Toolkit.
    
- Lazy queries.
    
- localStorage/sessionStorage persistence.
    
- pagination.
    
- debounce/throttle patterns.
    
- `React.memo`.
    
- `useMemo`.
    
- `useCallback`.
    
- lazy/on-demand loading.
    
- virtualized lists with React Window.
    
- Intersection Observer.
    
- Socket-driven incremental refresh.
    

Not every optimization in the entire CRM was implemented by me. My confirmed ownership is specifically the ticket-processing performance/cache/synchronization strategy described above and the frontend workflow I maintained.

## Collaboration Model

CRM was developed by a larger engineering group rather than as a solo project.

My working environment included:

- Frontend developers.
    
- Backend developers.
    
- Bách Khoa collaborators/team.
    
- Dedicated UI/design team.
    
- Dedicated testing/QA team.
    
- Business/manager stakeholders.
    
- Actual operational users.
    

A previously documented working structure included roughly **3 frontend + 2 backend developers** in the core CRM development collaboration, with additional design/testing/business participants around the project.

### Design

I did not claim ownership of the overall CRM visual design because a dedicated design team existed.

My responsibility was to:

- translate approved design/business flow into working UI;
    
- identify interaction issues during implementation;
    
- propose frontend-flow/state improvements where necessary;
    
- adjust implementation based on real workflow constraints.
    

### Testing

There was a dedicated testing team.

My responsibility as developer still included:

- developer-side verification;
    
- reproduce/fix issues raised by test;
    
- integration testing with backend;
    
- UAT-related fixes;
    
- production bug investigation.
    

## Deployment & Release

CRM uses GitLab CI/CD and Docker-based deployment flows at system level.

The archived system supports environments including:

```
Development
→ UAT
→ Production
```

My code was released to both **UAT and PROD**.

I therefore gained practical experience with a real release lifecycle:

```
Implement
→ Local/Development Test
→ Commit / Team Review Process
→ UAT
→ QA / User Feedback
→ Fix
→ Production Release
→ Production Support
```

I was not necessarily the owner of the entire infrastructure/CI pipeline, but I worked within and shipped code through that deployment process.

## Production Context

The ticket-processing flow I worked on was used in real operations across EVNHCMC's local electricity units.

This distinction matters:

```
Not:
University Demo / Portfolio Prototype

But:
Real Users
+ Real Customer Requests
+ Concurrent Operations
+ UAT
+ Production
+ Performance Constraints
+ Cross-team Support
```

As a result, frontend decisions had direct operational consequences.

A pattern that makes four unnecessary requests on a local development machine may appear harmless. With many concurrent production users, the same behavior can materially increase backend load.

CRM was the project where I experienced this difference most clearly.

## System Data & Infrastructure Context

Although these areas were primarily backend/team-owned, understanding them was useful when debugging.

### Microsoft SQL Server

Main relational business data includes:

- customer-related entities;
    
- tickets;
    
- ticket events;
    
- distributions;
    
- users;
    
- permissions;
    
- organizations;
    
- shifts;
    
- operational configurations.
    

The backend supports primary database access and read-replica/reporting-oriented configurations.

### MongoDB

Used in selected document/message-oriented services such as internal chat/notification-related domains.

### Redis

Used for runtime concerns such as:

- session/token state;
    
- OTP/state;
    
- real-time/socket coordination;
    
- service runtime data.
    

### RabbitMQ

Used for communication between NestJS microservices.

### Elasticsearch

Used for search/indexing-related workloads such as customer/ticket/contact lookup.

### Kafka

Appears in synchronization/integration flows.

### MinIO

Used as object/file storage.

These technologies describe the CRM platform architecture, not technologies I independently designed or administered.

## External Integrations — System Context

The codebase contains integrations/configuration related to systems such as:

- CMIS.
    
- OMS.
    
- Data Warehouse.
    
- EVN customer applications/web channels.
    
- SMS.
    
- Call-center/softphone infrastructure.
    
- Callbot / Chatbot.
    
- Omni-channel services.
    
- QA.
    
- App Công Trường.
    
- Reporting systems.
    
- AI-agent related services.
    

My ticket frontend interacted with some of these workflows indirectly through backend APIs, but I do not claim to have built every integration.

## Hard Problems & Lessons

### Performance Must Be Evaluated at Production Scale

The largest lesson was that frontend performance is not only browser FPS.

Frontend request behavior can create backend/system load:

```
One extra request × One developer
≈ invisible

One extra request × Many users × Frequent interaction
≈ production infrastructure problem
```

This changed how I think about:

- when to fetch;
    
- what to cache;
    
- when to invalidate;
    
- server vs client responsibility;
    
- real-time events;
    
- user-perceived loading.
    

### Cache Invalidation Is a Real Engineering Problem

Using local cache solved repeated loading but introduced new consistency problems.

I learned that caching is not simply:

```
localStorage.setItem(...)
```

A usable cache strategy also needs:

```
When is data valid?
What event invalidates it?
Which tab/resource changed?
Should I refetch count or full list?
What if another user processes the ticket?
What if pagination changed?
What if filter changed?
```

Socket events became a key part of keeping the client cache synchronized with server state.

### Large Codebase Debugging

CRM taught me how to navigate code I did not author.

Instead of only knowing my React component, I became comfortable tracing:

```
Component
→ Hook
→ RTK Query / Service
→ Request
→ API Controller
→ Backend Service
→ Query / External Integration
```

This was especially useful when a bug was visible in frontend but its root cause was elsewhere.

### Workflow State Matters

Ticket processing made me understand why business systems should model explicit states.

A ticket cannot simply be "open/closed". Different states define:

- who owns it;
    
- who can act;
    
- which action is allowed;
    
- where it should appear;
    
- whether it can be transferred;
    
- whether another unit is collaborating;
    
- whether it is blocked;
    
- whether it is completed.
    

This experience later influenced how I thought about workflow/state design in other business applications.

### Team Standards Matter

CRM was also where I learned much more about:

- consistent React/TypeScript coding style;
    
- router organization;
    
- API call conventions;
    
- code review/team conventions;
    
- FE/BE contracts;
    
- UAT/production workflow;
    
- debugging before escalating;
    
- communication between specialized teams.
    

## Technical Debt & Trade-offs

CRM is a mature enterprise system, but the frontend performance solution I worked with also has trade-offs.

### Browser Cache Complexity

Using localStorage for ticket lists/counts/filter/paging can lead to:

- stale data;
    
- browser-storage growth;
    
- duplicated state between React/Redux/query cache/localStorage;
    
- difficult invalidation logic;
    
- harder debugging.
    

Socket-triggered invalidation mitigates this, but a future redesign could centralize cache policy more strongly in a server-state library rather than spreading responsibility across several persistence layers.

### Real-time Event Complexity

Multiple events occurring close together can cause repeated refreshes. Current source includes debounce logic to group socket bursts, but complex concurrent workflows still require careful event design/idempotency.

### Distributed Backend Complexity

The system uses multiple microservices, queues, databases and real-time gateways. This provides scale/separation but also increases operational and debugging complexity.

This is a system-level trade-off, not one I personally chose.

## If I Built My Frontend Area Again

If rebuilding the ticket-processing frontend with the knowledge I have now, I would consider:

- centralizing server-state caching and invalidation in RTK Query/TanStack Query rather than relying as much on raw localStorage;
    
- defining a formal cache-key strategy per filter/status/page;
    
- defining explicit socket event contracts for invalidation;
    
- using optimistic updates only where business rules make them safe;
    
- adding stronger runtime schema validation for API/socket payloads;
    
- adding E2E tests for ticket state transitions;
    
- adding performance instrumentation for API-call count, cache-hit rate and render time;
    
- measuring backend impact with proper dashboards rather than relying only on operational observations;
    
- documenting the ticket state machine formally;
    
- keeping frontend action permissions aligned with backend authorization;
    
- testing multi-user concurrency scenarios explicitly.
    

## What I Learned

### Frontend Engineering

- React/TypeScript in a large production codebase.
    
- React Router in complex enterprise navigation.
    
- RTK Query/API abstraction.
    
- Large business forms and tables.
    
- Pagination/filter persistence.
    
- Socket-driven UI synchronization.
    
- Client-side caching.
    
- Performance optimization.
    
- Real-world state management.
    

### Backend Understanding

Even without being the primary backend developer:

- reading NestJS controllers/services;
    
- tracing API behavior;
    
- understanding SQL-backed domain flows;
    
- identifying FE vs BE root cause;
    
- communicating reproducible backend issues.
    

### Software Engineering

- working in a multi-team codebase;
    
- requirement/business-flow analysis;
    
- dedicated design → development → QA → UAT → production workflow;
    
- production bug handling;
    
- release discipline;
    
- communicating with FE/BE/test/design/business stakeholders.
    

### Performance

The most important practical lesson:

> Performance is a system property. A frontend implementation can overload the backend even when the UI itself appears fast.

### Production Mindset

CRM taught me to ask:

```
Does it work?
→ Is it correct under real workflow?
→ What happens when many people use it?
→ What happens when another user changes the same data?
→ Does the user see stale state?
→ Where is the real root cause?
→ How will it behave after deployment?
```

## Current Status & References

EVNHCMC CRM is a **real production enterprise system** used for customer-care operations across EVNHCMC.

My contribution should be described specifically as:

> **Frontend Developer responsible for the local electricity-unit ticket-processing workflow, including requirement/business-flow analysis, React implementation, real-time synchronization, performance optimization, UAT/production delivery, and cross-stack debugging; also contributed to shift-supervisor UI.**

I should **not** be described as the owner of the full CRM backend, microservice architecture, overall UI design or QA process.

The project is the strongest evidence in my profile for working successfully inside a **large production software system with real users, real concurrency, performance constraints and cross-functional engineering collaboration**.

---

# PROJECT — LinguaPanda

## Overview
**Tên project:** LinguaPanda  
**Tên thesis:** AI-Powered Personalization English Learning Platform with Adaptive Assessment, Feedback and Learning Path  
**Loại project:** Bachelor Thesis / Solo Full-stack AI-integrated Learning Platform  
**Thời gian:** Gồm hai giai đoạn — pre-thesis/initial development và final thesis development, kéo dài từ cuối 2025 đến giữa 2026  
**Trạng thái:** Deployed MVP / Thesis Completed  
**Vai trò của tôi:** Solo Full-stack Developer, System Designer, Thesis Researcher, Product/UX Designer  
**Portfolio priority:** Flagship / Core Technical Project
LinguaPanda là đồ án tốt nghiệp tôi tự thiết kế và phát triển toàn bộ, từ problem analysis, research, system architecture, database design, backend, frontend, AI integration, asynchronous processing, deployment đến thesis evaluation.
Project không chỉ là một website học tiếng Anh có tích hợp LLM. Mục tiêu chính là xây dựng một learning system có khả năng đánh giá trình độ ban đầu theo hướng adaptive, tạo learning path theo từng learner, đánh giá sâu Writing/Speaking và sử dụng kết quả học trước đó để điều chỉnh kế hoạch học tiếp theo.
Hai repository chính:
```
lingua-core    → Backend / AI services / database / queues / infrastructure
lingua-portal  → Next.js web application
```
Hai repository là các thành phần của cùng một system, không phải hai project độc lập.
## Problem & Motivation
Project bắt đầu từ việc phân tích các hạn chế thường gặp ở những nền tảng học tiếng Anh hiện tại:
- Placement test thường là self-assessment hoặc một bộ câu hỏi cố định.
- Learner cùng level thường nhận một learning path tương tự nhau dù có điểm mạnh/yếu khác nhau.
- Writing và Speaking thường chỉ nhận điểm tổng hoặc feedback tương đối nông.
- Dictionary thường trả nghĩa từ nhưng thiếu context, collocation và cách sử dụng phù hợp.
- AI có thể hỗ trợ personalization nhưng output không nên được tin và lưu trực tiếp nếu chưa qua validation.
LinguaPanda tập trung giải quyết các vấn đề trên bằng một learning lifecycle liên kết:
```
Google Login
→ Onboarding Survey
→ CAT / IRT 3PL Placement
→ CEFR Estimate
→ Personalized Weekly Learning Plan
→ Lessons / Practice
→ Assessment
→ Writing / Speaking Feedback
→ Weakness Extraction
→ Next Learning Plan
```
Điểm quan trọng là các module không hoạt động độc lập. Output từ placement, onboarding và assessment được sử dụng lại để xây learning plan và điều chỉnh learning path sau đó.
## Target Users & Scope
MVP hướng tới self-directed English learners từ khoảng A1 đến B2 theo CEFR.
Các skill chính trong final thesis MVP:
- Reading
- Writing
- Speaking
Listening có một số experimental artifacts trong source nhưng không nằm trong scope chính của final validated MVP.
Các phần được chủ động để ngoài MVP:
- Full Listening support
- Mobile application
- Spaced Repetition System
- Large-scale learner study
- Official IELTS-equivalent grading
- Production-scale adaptive item calibration
## Core Features
### Smart Onboarding
Sau Google login, learner có thể hoàn thành onboarding survey cung cấp các thông tin như:
- learning goal
- target/certificate
- focus skills
- available study days
- planned study hours
- self-assessed experience
- learning context
- common difficulties
- additional learning preferences
Survey information không chỉ được lưu để hiển thị profile. Nó được sử dụng trực tiếp trong personalized learning plan generation.
System cũng cho phép skip onboarding/placement để learner có thể explore platform, đồng thời vẫn lưu trạng thái skip/completion.
### CAT / IRT 3PL Placement
Placement engine được xây dựa trên Computer Adaptive Testing và Item Response Theory 3-Parameter Logistic model.
Mỗi question có ba tham số:
```
a → discrimination
b → difficulty
c → guessing probability
```
Probability model:
```
P(θ) = c + (1 - c) / (1 + e^(-a(θ-b)))
```
Learner ability `θ` được cập nhật sau mỗi câu trả lời bằng Maximum Likelihood Estimation với Newton-Raphson iteration.
Sau khi cập nhật ability, system sử dụng Fisher Information để chọn question tiếp theo có giá trị đo lường phù hợp với current ability.
Flow tổng quát:
```
Start θ
→ Select Item
→ Learner Answers
→ Update θ
→ Compute Standard Error
→ Calculate Fisher Information
→ Select Next Item
→ Stop Condition
→ Map θ to CEFR
```
Current implementation còn có:
- grammar phase trước reading/passage phase
- passage continuity logic
- exposure penalty
- maximum question per passage
- standard error
- confidence interval
- maximum 20 questions
- early stopping khi đủ số câu tối thiểu và standard error thấp
CEFR mapping có threshold từ A1 đến C1, nhưng learning content chính vẫn tập trung A1–B2.
IRT item parameters hiện được assign heuristic dựa trên CEFR difficulty chứ chưa được calibrated từ large learner-response dataset. Vì vậy kết quả được xem là **heuristic CEFR placement**, không phải standardized certified placement test.
### Personalized Weekly Learning Plan
Sau placement, backend tập hợp nhiều loại learner context:
```
CEFR Estimate
+
Onboarding Survey
+
Learning Goals
+
Focus Skills
+
Available Days
+
Weekly Study Time
+
Recent Exercise Performance
+
Recent Writing/Speaking Weaknesses
+
Available Lessons / Practice Sessions
```
Context được gửi sang AI service để tạo weekly learning plan.
System sử dụng **structured context injection**, không phải full RAG. Backend query dữ liệu thật từ relational database rồi đưa structured context vào prompt.
AI trả về plan items có dạng:
```
day
position
item type
content reference
title
estimated minutes
skill
rationale
```
Trước khi lưu, output phải đi qua deterministic validation:
- day hợp lệ
- learner thực sự available trong ngày đó
- skill hợp lệ
- item type hợp lệ
- content reference tồn tại trong database
- không duplicate
- task count phù hợp
- time budget phù hợp
- due date nằm trong current week
- các constraint theo Sunday/review
AI output không được persist trực tiếp nếu chưa qua validation.
### Feedback-Driven Weakness Loop
System lấy các Writing/Speaking submissions gần đây và đọc criterion-level feedback.
Ví dụ:
```
Grammatical Range & Accuracy low
→ writing_grammar_accuracy

Pronunciation low
→ speaking_pronunciation
```
Weakness được đánh severity:
```
< 5.5       → high
5.5 – 6.0   → medium
6.0 – 6.5   → low
```
Các weakness signal được deduplicate và inject vào generation context để plan tiếp theo có thể ưu tiên remedial tasks.
Đây là personalization loop chính:
```
Practice
→ Assessment
→ Detailed Feedback
→ Weakness Detection
→ New Personalized Plan
→ Targeted Practice
```
### Lessons & Practice Sessions
System có hai loại learning content chính:
```
Lesson
├─ Theory
└─ Practice Questions

Practice Session
└─ Full Question Set
```
Question system hỗ trợ nhiều loại:
- single-choice MCQ
- multiple-choice MCQ
- fill in the blank
- matching
- dictation-related content
- Writing
- Speaking
- passage-based Reading
- partial Listening artifacts
Objective question types được grade synchronous.
Writing và Speaking được grade asynchronous vì cần AI/provider processing.
### Assessment Lifecycle
Exercise lifecycle:
```
in_progress
→ submitted
→ scored
```
Learner bắt đầu một lesson/practice assessment, trả từng question, sau đó complete session.
Objective answers được grade ngay trong request.
Subjective answers tạo async grading job và trả status về frontend để learner không phải chờ một HTTP request dài.
### Hybrid Writing Grading
Writing pipeline không dùng một prompt duy nhất để lấy score.
Flow:
```
Essay
→ Surface / Relevance Pre-check
→ LanguageTool
→ Custom Deterministic Grammar Rules
→ Grammar Evidence
→ Groq LLM Rubric Evaluation
→ Post-validation
→ Persist Structured Feedback
```
LanguageTool được self-hosted trong backend infrastructure.
LLM đánh giá theo IELTS-aligned formative criteria.
Sau LLM, system áp dụng thêm deterministic safeguards:
- normalize score bands
- verify evidence quote tồn tại trong original submission
- verify correction structure
- grammar severity ceiling
- off-topic guard
- Task Response cap
- recompute overall score
- validation warnings
- review/confidence signals
Ví dụ nếu deterministic grammar analysis đã tìm thấy nhiều lỗi medium/high nhưng LLM vẫn trả Grammar score quá cao, score có thể bị giới hạn bởi validator.
System chỉ cung cấp **IELTS-aligned formative feedback**, không claim official IELTS scoring equivalence.
### Speaking Assessment
Speaking dùng multi-provider pipeline vì transcript-only assessment không đủ để đánh giá pronunciation.
Frontend:
```
Microphone
→ MediaRecorder
→ WebM Audio
→ Multipart Upload
```
Backend:
```
Receive Audio
→ Temporary Storage
→ BullMQ Job
→ Immediate Submitted Response
```
Worker:
```
Audio
→ Groq Whisper
→ Transcript

Transcript
→ Groq LLM
→ Linguistic Criteria

Audio + Transcript
→ Azure Speech Pronunciation Assessment
→ Pronunciation Metrics

LLM Criteria + Azure Pronunciation
→ Merge
→ Persist Structured Feedback
```
Groq Whisper phụ trách transcription.
Azure Speech cung cấp pronunciation evidence như:
- accuracy
- fluency
- completeness
- prosody
- word-level pronunciation scores
Groq LLM đánh giá các linguistic criteria dựa trên transcript.
Nếu Azure Speech unavailable, pipeline vẫn có thể trả transcript-based feedback và đánh dấu Pronunciation là unavailable thay vì fail toàn bộ submission.
### Smart Dictionary
Dictionary sử dụng database-first strategy.
```
User Lookup
→ Search DictEntry
→ Search WordForm / Root Form
→ If found: Return Database Result
→ If missing: AI Generation
→ Validate
→ Persist
→ Future Lookups Use Database
```
AI-generated entry có thể gồm:
- headword
- IPA
- part of speech
- CEFR level
- word forms
- senses
- contextual definitions
- Vietnamese meanings
- example sentences
- translations
- synonyms / antonyms
- collocations
Một AI-generated entry được persist để những lookup sau không cần gọi LLM lại.
User cũng có personal vocabulary list với note/context.
SRS chưa nằm trong final MVP.
### Dashboard
Learner dashboard tổng hợp:
- current CEFR
- study streak
- study time
- vocabulary count
- completed lessons
- completed exercises
- weekly plan progress
- skill performance
- recent activity
- activity calendar
Backend tổng hợp nhiều nguồn dữ liệu thành một dashboard response để frontend không phải tự thực hiện nhiều request rời rạc.
### Admin
Admin MVP tập trung vào monitoring và governance:
- user management
- placement status
- onboarding status
- CEFR distribution
- platform statistics
- placement analytics
Backend có một số content-management APIs rộng hơn UI hiện tại, nhưng final admin frontend chưa expose toàn bộ content creation capability.
## System Architecture
Kiến trúc production:
```
                    ┌──────────────────────┐
                    │   Next.js Portal     │
                    │   React / TypeScript │
                    └──────────┬───────────┘
                               │ HTTPS
                               ↓
                    ┌──────────────────────┐
                    │        Nginx         │
                    │ Reverse Proxy / SSL  │
                    └──────────┬───────────┘
                               ↓
                ┌──────────────────────────────┐
                │ NestJS API Gateway           │
                │                              │
                │ Business Logic               │
                │ Authentication               │
                │ Validation                   │
                │ Prisma / Persistence         │
                │ BullMQ Worker Integration    │
                └────────┬───────────┬─────────┘
                         │           │
                    Prisma│           │ TCP MessagePattern
                         ↓           ↓
                  PostgreSQL   ┌─────────────────────┐
                               │ NestJS AI Service   │
                  Redis        │                     │
                    ↑          │ Prompt Construction │
                    │          │ Groq LLM            │
                  BullMQ       │ Groq Whisper        │
                               │ Azure Speech        │
                               │ LanguageTool        │
                               └─────────────────────┘
```
Backend là NestJS monorepo gồm:
```
apps/
├─ api-gateway
└─ ai-service

libs/
├─ shared
├─ ai-client
├─ bullmq
└─ jwt
```
Architectural boundary quan trọng:
> `api-gateway` sở hữu business logic và database persistence. `ai-service` xử lý AI/provider-specific work và không trực tiếp write vào database.
Điều này giúp probabilistic AI processing được isolate khỏi core domain/persistence layer.
## Backend — lingua-core
### Tech Stack
- NestJS 11
- TypeScript
- Prisma 6
- PostgreSQL 17
- Redis 7
- BullMQ
- Groq SDK / LLM
- Groq Whisper
- Azure Speech SDK
- Google OAuth2
- JWT
- Argon2
- LanguageTool
- Swagger
- Docker
- Docker Compose
- Nginx
- GitHub Actions
Một số documentation/tooling cũ trong repository có mention Gemini/OpenAI/FastAPI, nhưng final runtime architecture không sử dụng chúng làm core production path.
Gemini chủ yếu xuất hiện trong offline content-generation/seed tooling.
### API Gateway Modules
Các domain chính:
```
auth
onboarding-placement
learning
learning-plan
assessments
dictionary
reports
admin
users
```
### AI Service
AI service phụ trách:
- prompt construction
- Groq LLM inference
- learning-plan generation
- Writing rubric evaluation
- Speaking transcript evaluation
- Groq Whisper transcription
- Azure Speech pronunciation assessment
- LanguageTool integration
Service này được tách khỏi database ownership.
## Frontend — lingua-portal
### Tech Stack
- Next.js 16
- React 19
- TypeScript
- App Router
- TanStack Query
- Zustand
- Axios
- React Hook Form
- Zod
- Tailwind CSS
- Radix/shadcn-style UI
- Framer Motion
- Browser MediaRecorder API
- Browser Speech Synthesis API
### Route Structure
```
(auth)
(onboarding)
(main)
(learn)
(exercise)
(admin)
```
Các flow chính:
```
Login

Onboarding
├─ Survey
├─ Placement
└─ Placement Result

Main
├─ Dashboard
├─ Plan
├─ Plan History
└─ Profile

Learning
├─ Lessons
├─ Lesson Detail
├─ Practice Sessions
└─ Practice Detail

Exercises
├─ Standard Exercise
├─ Writing
├─ Speaking
└─ Result / Feedback

Dictionary
Vocabulary

Admin
├─ Overview
├─ Users
└─ Placement
```
Frontend dùng TanStack Query cho server-state fetching/polling và Zustand cho một số local application state.
Subjective grading result được poll định kỳ cho đến khi assessment chuyển sang `scored`.
## Database Design
Database dùng normalized relational model trên PostgreSQL với Prisma.
Final schema gồm khoảng 27 models/tables được chia theo domain:
```
User / Authentication
Onboarding
Placement / CAT
Learning Content
├─ Lesson
├─ Question
├─ Option
├─ Passage
└─ Practice Session
Assessment
├─ Exercise Record
├─ Answer
├─ Answer Detail
├─ AI Call
├─ Answer Evaluation
└─ Evaluation Criteria
Learning Plan
Dictionary
├─ Dict Entry
├─ Word Form
├─ Sense
├─ Example
├─ Collocation
└─ User Vocabulary
```
JSON/JSONB chỉ được dùng cho những payload có cấu trúc linh hoạt như AI criteria/theory metadata thay vì biến toàn bộ relational domain thành document storage.
Một design principle quan trọng là AI result được persist vào domain phù hợp:
```
Writing / Speaking Result
→ AnswerEvaluation
Learning Plan Output
→ LearningPlan / LearningPlanItem
Dictionary Output
→ DictEntry / Sense / Example / Collocation
```
Không dùng một bảng generic AI response làm source of truth cho toàn hệ thống.
## Authentication & Security
Authentication flow:
```
Google OAuth
→ Verify Google ID Token
→ Find/Create User
→ Generate Access JWT
→ Generate Refresh JWT
```
System không yêu cầu learner tạo local password.
Refresh token được hash trước khi persist để có thể invalidate session.
Backend sử dụng authorization guard và admin guard cho các protected/admin endpoints.
Frontend có Axios interceptor:
```
Request
→ Attach Access Token

401
→ Refresh
→ Retry Original Request
```
### Security Debt
Current MVP vẫn có một số điểm cần cải thiện nếu đưa lên production quy mô lớn:
- frontend token storage vẫn JavaScript-readable
- cookie/logout handling có thể harden hơn
- JWT deployment configuration cần chuẩn hóa secret naming/fallback
- file upload validation cho Speaking cần chặt hơn
- audit/session monitoring còn hạn chế
Không lưu bất kỳ secret/API key thật nào trong project knowledge record.
## Asynchronous Processing
BullMQ + Redis được dùng chủ yếu để tách AI latency khỏi HTTP lifecycle.
```
Submit Subjective Exercise
→ Create Job
→ Return Immediately
Worker
→ Run AI / Provider Pipeline
→ Persist Result
Frontend
→ Poll Result
→ Render When Scored
```
Redis đóng vai trò BullMQ message broker, không phải general-purpose cache/session store.
Design này tránh việc learner phải chờ một synchronous request kéo dài nhiều giây trong lúc LLM hoặc speech services xử lý.
## AI Reliability Strategy
Một design principle xuyên suốt project:
> AI output is treated as untrusted structured input until validated.
Patterns được áp dụng:
```
AI Output
→ Parse
→ Normalize
→ Validate
→ Check Database References
→ Apply Deterministic Constraints
→ Persist
```
Examples:
- learning plan không được lưu nếu reference ID không tồn tại
- schedule phải khớp learner available days
- plan item không được duplicate
- AI-generated scores bị check/cap bởi deterministic evidence
- off-topic Writing bị giới hạn score
- grammar evidence phải match original submission
- provider failure được degrade/fallback nếu có thể
Mục tiêu không phải loại bỏ uncertainty của AI mà là giới hạn ảnh hưởng của probabilistic output đối với business state.
## UI/UX Design Process
Design flow thực tế:
```
Problem / Product Idea
→ Feature List
→ Information Architecture / User Flow
→ Google Stitch hỗ trợ tạo visual ideas
→ Tôi chọn và redesign/refine lại
→ Final UI Direction
→ Tôi tự implement Next.js frontend
```
Tôi không coi Stitch output là final design tự động.
Tôi tự xây product direction, feature structure, UX flow và sau đó dùng Stitch như một ideation/prototyping assistant. Visual output được tôi chỉnh sửa/restructure trước khi implementation.
Design direction của platform thiên về **Academic Calm** và **progress over performance** thay vì gamification mạnh.
Một số UX principles:
- dashboard ưu tiên progress/streak/skill development
- focused mode khi làm exercise
- hide sidebar khi assessment
- reading passage và question panel có thể tách độc lập
- loading/error/empty states được thiết kế rõ
- learner luôn biết vị trí hiện tại trong learning journey
## Content Strategy
Learning content chính được prepare/seed vào database trước khi runtime.
```
Offline Content Preparation
→ CEFR-aligned Lesson / Practice Data
→ Seed Database
```
Một số offline tooling sử dụng AI để hỗ trợ tạo content JSON theo skill/CEFR/topic, nhưng runtime learner không nhận một lesson hoàn toàn generated on demand mỗi lần học.
Runtime AI tập trung vào:
- personalization
- grading
- feedback
- dictionary fallback
Điều này giúp content base ổn định hơn và giảm phụ thuộc vào LLM cho core curriculum.
## Deployment & Infrastructure
Final deployment:
```
Frontend
→ Vercel
→ lingua-panda.io.vn
Backend Infrastructure
→ Vietnix VPS
→ Ubuntu 24.04
→ Nginx
→ Docker Compose
   ├─ PostgreSQL 17
   ├─ Redis 7
   ├─ LanguageTool
   ├─ api-gateway
   └─ ai-service
API
→ api.lingua-panda.io.vn
```
Frontend được host chính trên Vercel.
Repository có Docker/VPS frontend deployment experiment nhưng flow đó bị disable và không phải main production deployment.
### CI/CD
Backend CI:
```
Push / Merge
→ GitHub Actions
→ Install
→ Prisma Generate
→ Type Check
→ Build Verification
```
Controlled deployment:
```
Manual CD
→ SSH VPS
→ Sync Repository
→ Apply Prisma Migration
→ Build / Restart Containers
→ Health Check
→ Cleanup
```
Deployment workflow có kiểm tra trạng thái và rollback-oriented logic khi deploy fail.
## Testing & Evaluation
Evaluation trong thesis tập trung vào việc xác nhận hệ thống hoạt động đúng với objectives của MVP:
- full learner journey functional testing
- Swagger/API verification
- CAT algorithm behavior
- learning-plan validation
- Writing/Speaking grading pipeline behavior
- frontend/backend integration
- deployment verification
- qualitative comparison với existing platforms
Automated test coverage hiện chưa mạnh và không được claim là comprehensive test suite.
Project **chưa có external learner testing** ở thời điểm final thesis.
Không có large-scale experiment hay formal user study.
Do đó các kết luận về educational effectiveness, placement accuracy hoặc grading accuracy được xem là preliminary/system-level validation chứ không phải validated result từ một learner population lớn.
## Technical Decisions
### NestJS for Both API and AI Service
Thay vì dùng hai technology ecosystems khác nhau, cả API Gateway và AI Service đều dùng NestJS/TypeScript.
Điều này giúp:
- shared DTO/enums
- shared validation
- consistent tooling
- type reuse
- monorepo maintenance
- simpler deployment
### Separate AI Service
AI/provider logic được tách để core business service không bị gắn chặt vào Groq/Azure/LanguageTool implementation.
### PostgreSQL + Prisma
Relational database phù hợp vì các domain có nhiều relationship rõ: learner, assessment, lesson, question, plan, dictionary, vocabulary.
### BullMQ + Redis
AI workload có latency cao nên queue giúp tránh block request lifecycle.
### Database-first Dictionary
AI chỉ được gọi khi dữ liệu chưa tồn tại, giảm repeated token usage và biến generated result thành reusable domain data.
### Structured Context Instead of Full RAG
Learning-plan personalization cần learner state có cấu trúc rõ ràng; vì vậy relational queries + structured prompt context đơn giản và dễ validate hơn vector retrieval đối với MVP.
### Deterministic Validators Around AI
LLM không được xem là authoritative source cho score/business state.
### Vercel + VPS Split
Frontend có thể deploy độc lập nhanh, trong khi backend/data/queues/self-hosted services nằm trên VPS cần nhiều runtime control hơn.
## Challenges
### Designing Adaptive Placement
Challenge không chỉ là implement công thức IRT mà còn là:
- ability update stability
- next-item selection
- standard error
- stopping criterion
- passage continuity
- content difficulty
- CEFR mapping
- tránh claim accuracy cao hơn evidence
### Constraining AI Grading
Một LLM có thể trả output hợp lệ về JSON nhưng không hợp lý về pedagogy.
Writing pipeline cần thêm rule-based evidence và post-validation để giảm inconsistency.
### Speaking Requires Multiple Evidence Sources
Transcript không chứa đầy đủ pronunciation/prosody signal, nên system phải phối hợp Whisper, Azure Speech và LLM thay vì chỉ dùng một provider.
### Personalized Plan Must Reference Real Content
AI-generated text plan không có giá trị nếu nó tham chiếu lesson không tồn tại hoặc schedule không phù hợp learner availability.
Backend phải validate reference và schedule trước khi persistence.
### Async User Experience
AI jobs mất thời gian xử lý nhưng learner vẫn phải tiếp tục sử dụng app bình thường. Queue + polling được chọn để tách UX khỏi provider latency.
### Deployment Within Thesis Budget
Infrastructure phải đủ để chạy:
- database
- Redis
- LanguageTool
- API service
- AI service
trong khi vẫn giữ chi phí phù hợp với solo thesis project.
## Limitations & Technical Debt
### CAT Calibration
IRT parameters chưa được empirically calibrated từ large-scale learner response data. Placement output là heuristic estimate.
### AI Grading Validation
Chưa có formal comparison với human raters. Feedback được xem là educational/formative support.
### External User Testing
Chưa có independent learner/user testing ở final thesis stage.
### Speaking Limitations
Transcript-based criteria không phản ánh hoàn toàn pause length, hesitation, natural delivery hoặc conversational quality.
Azure dependency cũng có thể ảnh hưởng pronunciation availability.
### Listening & Mobile
Listening chưa hoàn thành trong validated MVP.
Mobile app chưa phát triển.
### SRS
Vocabulary system chưa có spaced-repetition scheduling.
### Queue Failure Recovery
Explicit user-facing failure/retry state cho AI job có thể được cải thiện.
### Audio Storage
Temporary local audio storage chưa phải ideal architecture nếu cần horizontal scaling/container restart resilience.
### Security Hardening
Token/cookie/session configuration và upload validation cần harden trước production-scale usage.
### Observability
Logging đã có nhưng monitoring, metrics, alerting, provider fallback và distributed tracing chưa ở mức production platform lớn.
## What I Learned
LinguaPanda là project tổng hợp gần như toàn bộ technical knowledge mạnh nhất của tôi ở thời điểm hiện tại.
### Product & Research
- problem analysis
- literature review
- requirements
- feature prioritization
- scope control
- MVP decisions
- distinguishing research claim from implementation claim
### Backend Engineering
- NestJS architecture
- monorepo organization
- modular services
- DTO/validation
- REST API
- TCP service communication
- Prisma/PostgreSQL
- JWT/OAuth
- queues and workers
### Frontend Engineering
- Next.js App Router
- React/TypeScript
- server-state management
- form validation
- assessment UI
- audio recording
- async result UX
- admin/learner route separation
### Database
- normalized relational modeling
- domain separation
- JSON/JSONB where justified
- persistence of AI output into structured domain entities
### Applied AI
- LLM provider integration
- prompt construction
- structured output validation
- AI fallback strategy
- speech transcription
- pronunciation assessment
- deterministic + AI hybrid evaluation
### Algorithms
- IRT 3PL
- Maximum Likelihood Estimation
- Newton-Raphson
- Fisher Information
- adaptive item selection
- threshold/stopping design
### Infrastructure
- Docker
- Docker Compose
- Ubuntu VPS
- Nginx
- PostgreSQL
- Redis
- self-hosted LanguageTool
- GitHub Actions
- Vercel
- domains / HTTPS / deployment
### Engineering Mindset
Project reinforced several principles:
```
AI output must be validated.
Algorithm implementation does not imply empirical accuracy.
System boundaries matter more than using many technologies.
Async workloads should not block user interaction.
Domain data should remain source of truth.
Architecture should reflect actual failure modes and constraints.
```
## If I Rebuild or Continue
Priority improvements:
- empirically calibrate CAT item parameters using real learner responses
- perform learner study with a larger participant group
- compare AI grading against human raters
- add Listening
- implement SRS for vocabulary
- build mobile client
- improve job failure/retry UX
- move audio/object storage to durable external storage
- harden authentication/token handling
- add strong automated unit/integration/e2e tests
- add monitoring/metrics/alerting
- introduce AI provider fallback
- evaluate full RAG only where semantic retrieval provides measurable value
- improve content-management tools for Admin
## Current Status & References
LinguaPanda reached a complete thesis MVP and was deployed publicly.
**Frontend:** `https://lingua-panda.io.vn`  
**Backend API:** `https://api.lingua-panda.io.vn`
The project should be treated as one of the primary flagship projects in my technical profile.
It is the clearest representation of my current strengths in:
> **Full-stack TypeScript development, system architecture, relational database design, asynchronous processing, applied AI integration, adaptive assessment algorithms, validation-oriented engineering, and deployment.**

---

# PROJECT — eSign

## Overview
**Tên project:** eSign — Employee Contract Management & Approval System  
**Trạng thái:** Internal Development / Testing  
**Loại project:** Internal Business Application — EVNHCMC  
**Vai trò của tôi:** Full-stack Developer / Main Developer  
**Portfolio priority:** Medium — Real-world Supporting Project
	eSign là hệ thống nội bộ phục vụ **tạo, xác nhận, theo dõi và lưu trữ hợp đồng lao động** của nhân viên EVNHCMC.
	Tên project là eSign nhưng archived system **không thực hiện cryptographic digital signing**. Tại thời điểm phát triển, đơn vị chưa có hạ tầng/đăng ký chữ ký số phù hợp, vì vậy hợp đồng sau khi được xác nhận trong hệ thống vẫn được **in, trình ký/đóng dấu theo quy trình thực tế**, sau đó scan và upload trở lại hệ thống để lưu trữ.
	Tôi là developer chính của project và phụ trách từ requirement analysis, solution design, database, backend/frontend, HRMS integration đến testing với manager/người dùng nội bộ.
## Business Context & Workflow
Requirement được xây dựa trên nhu cầu số hóa quy trình hợp đồng lao động thay vì xử lý thủ công từ đầu đến cuối.
Hệ thống sử dụng dữ liệu có sẵn từ HRMS:
```
EVN HRMS
├─ Employee
├─ Organization
├─ Department
├─ Position
├─ Salary Grade
└─ Salary
        ↓
eSign Contract Workflow
```
Manager có thể filter nhân viên theo đơn vị/phòng ban, chọn một hoặc nhiều người và tạo hợp đồng nhanh.
Workflow thực tế:
```
Manager chọn nhân viên từ HRMS
→ Tạo 1 hoặc nhiều hợp đồng
→ Fill / generate contract information
→ Gửi cho Employee

Employee đăng nhập tài khoản nội bộ
→ Kiểm tra hợp đồng
→ Bổ sung/xác nhận thông tin
→ Gửi lại Manager

Manager kiểm tra lần cuối
→ Xác nhận
→ Chuyển lên cấp có thẩm quyền

Ngoài hệ thống:
→ In hợp đồng
→ Ký / đóng dấu
→ Cấp số hợp đồng

Sau đó:
→ Scan signed/stamped contract
→ Upload lại eSign
→ Lưu trữ và quản lý trạng thái
```
State workflow được thiết kế theo tư duy tương tự state machine đã dùng trong CRM: mỗi hồ sơ/hợp đồng đi qua các trạng thái rõ ràng thay vì xử lý bằng các flag rời rạc.
Archived code định nghĩa các trạng thái như:
```
PENDING_EMPLOYEE_CONFIRM
→ PENDING_MANAGER_CONFIRMED
→ CONFIRMED

+ CANCELLED
+ EXPIRED
```
## Core Features
### HRMS Employee Search
Manager có thể tìm/filter nhân viên theo:
- Organization.
- Department.
- Position.
- Employee information.
- Các thông tin nhân sự liên quan.
Dữ liệu này được lấy từ HRMS thay vì nhập lại hoàn toàn.
### Contract Creation
Hệ thống hỗ trợ:
- Tạo hợp đồng cho một employee.
- Bulk create hợp đồng cho nhiều employee.
- Tạo nhanh theo đơn vị/phòng ban.
- Điền thông tin hợp đồng.
- Contract type.
- Start/end date.
- Organization/department/position.
- Salary information.
- Employer/representative information.
- Legal/document information.
Backend sử dụng transaction để tránh tình trạng tạo dữ liệu dở dang và có logic xử lý employee không tồn tại hoặc đang có pending contract.
### Employee Confirmation
Employee đăng nhập bằng tài khoản nội bộ.
Nếu employee chưa có account tương ứng trong database, backend có thể tạo account dựa trên thông tin xác thực/nội bộ và mapping employee.
Employee xem nội dung hợp đồng, bổ sung/xác nhận thông tin cần thiết rồi submit lại cho manager.
### Manager Approval
Manager kiểm tra hợp đồng sau employee confirmation và xác nhận trước khi hồ sơ được chuyển sang bước xử lý ngoài hệ thống để ký/đóng dấu.
### Contract Document Generation
Backend có Word template và sử dụng:
```
PizZip
+ Docxtemplater
```
để inject dữ liệu từ hệ thống vào contract document.
Flow:
```
Employee / Contract / Salary Data
→ DOCX Template
→ Docxtemplater
→ Generated Employment Contract
```
Các dữ liệu được fill gồm employer, representative, legal document, employee, identification information, organization, department, position, salary, contract dates và contract type.
### Signed Document Storage
Sau khi hợp đồng được in, ký/đóng dấu và cấp số ngoài hệ thống, bản scan có thể được upload trở lại eSign để:
- View.
- Download.
- Lưu trữ.
- Thay thế/cập nhật file hợp đồng đã hoàn tất.
## Tech Stack
**Frontend:** Next.js 14, React 18, TypeScript, Redux Toolkit, Axios, Ant Design, Tailwind CSS, Zod, PDF viewer, Chart.js.  
**Backend:** NestJS, TypeScript.  
**ORM/Data Access:** Sequelize / sequelize-typescript; raw `mssql` cho một số integration.  
**Database:** Microsoft SQL Server.  
**Authentication:** JWT, bcrypt, LDAP/Active Directory integration.  
**HR integration:** EVN HRMS.  
**Document generation:** Docxtemplater, PizZip.  
**Other:** PDF tooling, Nodemailer, Swagger.  
**Infrastructure:** Docker, GitLab CI/CD, container registry và server deployment pipeline.
## Architecture
```
Next.js Portal
        ↓
NestJS API
        ↓
SQL Server
        ↕
EVN HRMS / Internal Identity
        ↓
Contract Workflow
        ↓
DOCX Generation / File Storage
```
Authentication hỗ trợ local/internal account và Active Directory-related flow. JWT payload chứa thông tin employee/organization/department/position/user level để phục vụ authorization và data filtering theo phạm vi đơn vị.
## My Contribution
Manager đưa business requirement; tôi tự phân tích quy trình hiện tại, đề xuất solution và trình bày cho Phó phòng để review/xác nhận trước khi implementation.
Quy trình làm việc thực tế:
```
Manager Requirement
→ Analyze Current Process
→ Design Workflow / State
→ Propose Solution
→ Review with Department Manager
→ Database Design
→ Backend
→ Frontend
→ HRMS / Authentication Integration
→ Internal Test
→ Manager/User Feedback
→ Fix & Iterate
→ Deploy for Internal Testing
```
Tôi phụ trách chính:
- Requirement analysis.
- Contract workflow/state design.
- Database design.
- NestJS backend.
- Next.js frontend.
- HRMS employee integration.
- Authentication/account mapping.
- Employee/manager flows.
- Single/bulk contract creation.
- Contract status transitions.
- DOCX generation.
- Contract file upload/view/download.
- Testing, bug fixing và iteration theo feedback.
- Deployment phục vụ internal testing.
Project được phát triển sau CRM và trước e-Retire.
## Technical Notes & Decisions
### Workflow State Instead of Boolean Flags
Một quyết định quan trọng là đưa contract qua các state rõ ràng. Cách tiếp cận này chịu ảnh hưởng từ workflow đã sử dụng trong CRM:
```
CRM idea:
Pending
→ Processing
→ Done

eSign:
Pending Employee Confirmation
→ Pending Manager Confirmation
→ Confirmed
```
Việc dùng state giúp frontend/backend biết rõ action nào được phép tại từng bước và giảm ambiguity trong business flow.
### HRMS as Source of Employee Data
Thay vì nhập lại employee/organization/position/salary data, hệ thống tái sử dụng HRMS làm nguồn dữ liệu chính. Điều này giảm duplicate input và phù hợp với hệ thống nội bộ EVN.
### Bulk Contract Creation
Bulk creation giải quyết trường hợp manager cần tạo hợp đồng cho nhiều nhân viên cùng phòng/đơn vị thay vì thao tác từng người.
### Hybrid Digital/Physical Workflow
Do chưa có chữ ký số, eSign không cố giả lập việc ký điện tử. Hệ thống số hóa các bước có thể số hóa:
```
Employee Selection
→ Data Preparation
→ Confirmation
→ Approval Tracking
→ Document Generation
→ Storage
```
còn bước ký/đóng dấu vẫn diễn ra ngoài hệ thống, sau đó kết quả được scan/upload lại.
## Limitations, Technical Debt & Lessons
Giới hạn lớn nhất là quy trình chưa thể end-to-end digital vì chưa tích hợp chữ ký số/CA provider. Việc in, đóng dấu, lấy số và scan tạo ra một đoạn manual workflow giữa `CONFIRMED` và bản hợp đồng cuối cùng.
Project chủ yếu ở mức internal development/testing, chưa có bằng chứng về long-term production usage hoặc load lớn.
Nếu phát triển tiếp, hướng quan trọng nhất là:
- Tích hợp digital signature/CA.
- Audit trail đầy đủ cho từng action.
- Approval hierarchy rõ hơn.
- Notification/reminder workflow.
- Versioning cho contract/document.
- Stronger authorization testing.
- Monitoring và operational logging.
- E2E/automated tests.
Project giúp tôi hiểu sâu hơn cách chuyển một quy trình giấy tờ nội bộ thành workflow software, cách modeling state, tích hợp HRMS/AD, generate business documents và làm việc trực tiếp với manager/user để refine requirement.
## Current Status & References
eSign là internal EVNHCMC application được xây để số hóa phần lớn quy trình hợp đồng lao động nhưng **không được mô tả là hệ thống ký số hoàn chỉnh**.
Giá trị chính trong profile là kinh nghiệm full-stack thực tế, workflow/state design, HRMS/AD integration, document generation và việc tự đưa một business requirement từ phân tích đến internal testing/deployment.

---

# PROJECT — e-Retire
## Overview
**Tên project:** e-Retire — Retirement Information & Spending Management System  
**Trạng thái:** Completed Development / Pending Rollout  
**Loại project:** Internal Business Application — EVNHCMC  
**Vai trò của tôi:** Full-stack Developer / Main Developer  
**Portfolio priority:** Medium — Real-world Supporting Project
	e-Retire được xây để giải quyết một vấn đề vận hành thực tế tại EVNHCMC: thông tin cán bộ hưu trí trước đây chủ yếu được các đơn vị quản lý bằng **Excel riêng lẻ**, dẫn đến dữ liệu phân tán, khó chuẩn hóa và khó tổng hợp ở cấp Tổng công ty.
	Mục tiêu của hệ thống là đưa thông tin cán bộ hưu trí về một hệ thống chung, cho phép Tổng công ty và các đơn vị địa phương quản lý dữ liệu nhất quán, tra cứu nhanh và ghi nhận các khoản chi/chăm sóc phát sinh trong suốt quá trình quản lý cán bộ hưu trí.
	Tôi là developer chính của project và tự phụ trách phần lớn quy trình từ phân tích yêu cầu, đề xuất giải pháp, thiết kế database, backend, frontend, integration đến testing với người dùng nội bộ.
## Business Context & Scope
User mục tiêu là các nhân viên phụ trách **nhân sự / quản lý cán bộ hưu trí**, bao gồm manager tại Tổng công ty và các đơn vị điện lực địa phương.
Business problem chính:
```
Nhiều file Excel tại các đơn vị
→ Dữ liệu không đồng nhất
→ Khó tra cứu / tổng hợp
→ Khó quản lý lịch sử thông tin
→ Khó ghi nhận các khoản chi liên quan cán bộ hưu trí
```
e-Retire chuẩn hóa quy trình thành:
```
HRMS / Employee Data
→ Retirement Information
→ Organization-based Management
→ Spending / Support History
→ Centralized Search & Reporting
```
## Core Features
### Retirement Information Management
Hệ thống cho phép:
- Quản lý danh sách cán bộ hưu trí.
- Tìm kiếm theo mã nhân viên hoặc tên.
- Filter theo đơn vị.
- Filter theo năm nghỉ hưu.
- Thêm/cập nhật thông tin.
- Quản lý thông tin liên hệ.
- Quản lý thông tin ngân hàng.
- Quản lý avatar.
- Export dữ liệu Excel.
Dữ liệu nhân sự và cơ cấu tổ chức được tích hợp từ HRMS để giảm nhập liệu thủ công và giữ liên kết với hệ thống nhân sự hiện có.
Khi một nhân viên được chuyển sang trạng thái hưu trí, hệ thống lưu các thông tin lịch sử quan trọng như đơn vị và chức danh tại thời điểm nghỉ hưu, đồng thời cho phép xác định đơn vị hiện đang chịu trách nhiệm quản lý người đó.
### Spending & Support History
Một yêu cầu nghiệp vụ quan trọng là ghi nhận các khoản chi liên quan đến cán bộ hưu trí.
Các khoản này có thể phát sinh từ nhiều sự kiện trong năm, ví dụ:
- Sinh nhật.
- Tết.
- Ngày kỷ niệm/ngày truyền thống của ngành.
- Các chương trình chăm sóc cán bộ hưu trí.
- Thăm hỏi.
- Phúng điếu khi cán bộ hưu trí qua đời.
- Các khoản hỗ trợ khác theo từng đợt.
Thay vì lưu rời rạc, hệ thống cho phép tạo một **đợt chi**, xác định lý do, ngày chi, danh sách người nhận, số tiền và thông tin ngân hàng liên quan.
Data model về mặt nghiệp vụ có dạng:
```
Spending
├─ Spending Reason
├─ Spending Date
├─ Total Amount
└─ Spending Details
   ├─ Retiree
   ├─ Amount
   ├─ Bank
   └─ Bank Account
```
Điều này giúp lưu được lịch sử chăm sóc/chi trả cho từng cán bộ hưu trí thay vì chỉ quản lý thông tin hồ sơ.
### User & Organization Management
Hệ thống có user management và phân quyền theo level/đơn vị.
Các level trong archived implementation gồm:
```
NORMAL
ADMIN
SUPER_ADMIN
```
User có thể được giới hạn phạm vi quản lý theo organization, phù hợp với mô hình Tổng công ty và các đơn vị trực thuộc.
## Tech Stack
**Frontend:** Next.js, React, TypeScript, React Query, Redux Toolkit, Axios, React Hook Form, Zod, Ant Design, Shadcn/Radix, Tailwind CSS.  
**Backend:** NestJS, TypeScript.  
**ORM:** Prisma.  
**Database:** PostgreSQL.  
**Authentication:** JWT access/refresh token, Argon2id password hashing.  
**Integration:** EVN HRMS; có implementation liên quan LDAP/Active Directory.  
**Reporting:** ExcelJS / Excel export.  
**API documentation:** Swagger/OpenAPI.
## Architecture & Data Design
Kiến trúc chính:
```
Next.js Portal
→ API / Query Layer
→ NestJS Core
→ Prisma
→ PostgreSQL
        ↕
EVN HRMS
```
Một quyết định data design đáng chú ý là không chỉ reference employee hiện tại mà còn lưu **snapshot thông tin tại thời điểm nghỉ hưu**, ví dụ:
```
Employee
→ Retirement

employeeCode
employeeName
dateOfBirth
gender

originalOrganization
originalPosition

currentManagementOrganization
retirementManagerDepartment

contactInformation
bankInformation
retirementDate
lifeStatus
```
Việc lưu cả ID và tên của một số thông tin lịch sử giúp tránh việc thay đổi cơ cấu/tên gọi trong HRMS làm mất ý nghĩa lịch sử của dữ liệu hưu trí.
## My Contribution
Requirement ban đầu được manager đưa ra dưới dạng nhu cầu nghiệp vụ. Tôi tự phân tích vấn đề hiện tại, xây hướng giải quyết và trình bày solution cho **Phó phòng** phụ trách để review/xác nhận trước khi implementation.
Quy trình tôi thực hiện:
```
Business Requirement
→ Requirement Analysis
→ Proposed Solution
→ Review / Confirmation
→ Database Design
→ Backend Development
→ Frontend Development
→ HRMS Integration
→ Internal Testing
→ User/Manager Validation
```
Tôi trực tiếp phụ trách:
- Phân tích requirement.
- Thiết kế solution.
- Database/schema design.
- Backend NestJS.
- Frontend Next.js.
- HRMS integration.
- Authentication/authorization flow.
- Spending management.
- Retirement information management.
- User/organization management.
- Testing và bug fixing.
- Demo/test với nhân viên và manager nội bộ.
Project về cơ bản được hoàn thành về development. Tuy nhiên trước khi rollout chính thức, tôi phải dừng công việc tại EVN để tập trung hoàn thành chương trình đại học, vì vậy hệ thống hiện ở trạng thái **pending rollout** thay vì được ghi nhận là production-wide deployment.
## Technical Notes & Decisions
Business requirement quan trọng nhất không phải CRUD mà là **chuẩn hóa dữ liệu phân tán từ nhiều đơn vị**.
Việc tích hợp HRMS giúp tránh duplicate data entry cho employee/organization. Trong khi đó, dữ liệu retiree cần lưu thêm snapshot lịch sử vì thông tin tổ chức/chức danh trong HRMS có thể thay đổi theo thời gian.
Spending được thiết kế thành header/detail thay vì lưu một record tiền trực tiếp trên retiree, vì một sự kiện có thể áp dụng cho nhiều cán bộ hưu trí và mỗi người có amount/bank information riêng.
## Limitations, Technical Debt & Lessons
Project chưa trải qua rollout rộng và production usage dài hạn, vì vậy chưa có dữ liệu thực tế để đánh giá performance/load hay operational issues ở quy mô toàn EVNHCMC.
Nếu tiếp tục phát triển, các phần cần quan tâm thêm gồm migration từ Excel cũ, data validation/duplicate handling, audit history, permission testing giữa các đơn vị, backup/recovery và monitoring sau deployment.
Project giúp tôi có kinh nghiệm thực tế trong việc chuyển một quy trình đang dựa trên Excel thành một hệ thống tập trung, đặc biệt ở các bước requirement analysis, database modeling, organization-based authorization, HRMS integration và trao đổi solution trực tiếp với business stakeholder.
## Current Status & References
e-Retire là một internal EVNHCMC application đã hoàn thành phần development và internal validation nhưng **chưa rollout chính thức** tại thời điểm tôi kết thúc công việc ở EVN.
Project được giữ trong profile như một real-world full-stack project thể hiện khả năng tự nhận requirement, phân tích nghiệp vụ và xây một business system end-to-end.

---

# PROJECT — AI-Based Automatic Student Attendance Device for School Buses
## Overview
**Tên sử dụng trong CV:** AI-Based Automatic Student Attendance Device for School Buses  
**Tên công trình công bố:** Thiết bị điểm danh tự động học sinh trên xe buýt sử dụng trí tuệ nhân tạo  
**Thời gian:** Tham gia từ giai đoạn khởi đầu của project; active development khoảng 2024–2025  
**Trạng thái:** Research Prototype / Functional Demo  
**Loại project:** Scientific Research Project — International University - VNUHCM & HUTECH collaboration  
**Vai trò của tôi:** Core Research Member, Flutter Developer, Requirements & Application Flow Contributor, Database Design Contributor, Figma Designer  
**Portfolio priority:** High — Research / Innovation Project
	Project xuất phát từ một vấn đề an toàn thực tế: học sinh tiểu học có thể bị bỏ quên trên xe đưa đón. Thay vì chỉ phụ thuộc vào việc kiểm tra thủ công, nhóm nghiên cứu đề xuất một hệ thống sử dụng camera và nhận diện khuôn mặt để ghi nhận học sinh khi **lên xe** và kiểm tra lại khi **xuống xe**, từ đó phát hiện trường hợp bất thường và thông báo trạng thái cho phụ huynh.
	Tôi là một trong ba thành viên tham gia từ giai đoạn đầu của project. Nhóm sau đó mở rộng thành khoảng 10 thành viên cùng 2 giảng viên hướng dẫn từ IU và HUTECH.
## Research Problem & Objective
Mục tiêu chính là giảm nguy cơ học sinh bị bỏ quên trên xe đưa đón bằng cách xây dựng một attendance flow hai bước:
```
Học sinh lên xe
→ Camera ghi nhận khuôn mặt
→ Backend nhận diện học sinh
→ Đánh dấu trạng thái "đã lên xe"
→ Đồng bộ dữ liệu
→ Thông báo cho phụ huynh

Xe đến trường
→ Quét lại khuôn mặt khi học sinh xuống xe
→ Backend nhận diện lại
→ Đánh dấu trạng thái "đã xuống xe"
→ Đối chiếu danh sách lên / xuống
→ Thông báo cho phụ huynh
→ Cảnh báo nếu còn học sinh chưa được ghi nhận xuống xe
```
Ngoài attendance, hệ thống còn hướng tới việc cung cấp vị trí xe/hành trình để phụ huynh có thể theo dõi trạng thái di chuyển của học sinh.
## Research System & Face Recognition Flow
Ở mức toàn hệ thống nghiên cứu, công trình mô tả pipeline nhận diện khuôn mặt gồm:
- Camera ghi nhận hình ảnh học sinh.
- Face detection/alignment bằng MTCNN.
- Feature extraction bằng Inception-ResNet.
- Biểu diễn khuôn mặt dưới dạng vector đặc trưng 512 chiều.
- So sánh embedding bằng Cosine Similarity và Euclidean Distance.
- Cập nhật attendance result và đồng bộ dữ liệu về server.
Phần AI model/backend **không phải implementation của tôi**. Hai thành viên khác phụ trách backend và AI training/recognition pipeline.
Contribution của tôi trong face-recognition flow là phía application:
```
Flutter Camera
→ Capture face image
→ Gửi image lên backend
→ Backend kiểm tra / nhận diện so với dữ liệu đã đăng ký
→ App nhận kết quả và cập nhật UI / trạng thái
```
Trong mobile app, tôi cũng tích hợp Google ML Kit Face Detection để kiểm tra ảnh có chứa khuôn mặt trước khi upload, nhưng không claim đây là face-recognition model chính của research system.
## Mobile Application Scope
Mobile app được xây bằng Flutter/Dart và có nhiều role: **Parent, Teacher, Driver, Admin**.
Các chức năng chính của hệ thống gồm authentication theo role, student information, parent/teacher/driver information, student attendance status, notification khi học sinh lên/xuống xe, Safe/Emergency/Solved states, bus information và attendance count, absent/student lists, tracking/location concept cho hành trình xe, student image registration, camera capture và upload ảnh khuôn mặt, feedback/settings/profile và các màn quản trị student/parent/teacher/driver/bus route/notification.
## Tech Stack
**Mobile:** Flutter, Dart.  
**Local persistence:** SharedPreferences và local application state.  
**Networking:** REST API, Bearer token ở một số flow.  
**Camera:** Flutter camera integration.  
**Face detection on device:** Google ML Kit Face Detection.  
**Backend:** Research-team backend service.  
**AI / Face Recognition:** MTCNN + Inception-ResNet pipeline do các thành viên AI/backend khác phụ trách.  
**Design:** Figma.  
**Target platforms:** Android/iOS Flutter application.
## Architecture
Ở góc nhìn application:
```
Flutter Mobile App
├─ Parent Module
├─ Teacher Module
├─ Driver Module
└─ Admin Module
        ↓
REST API
        ↓
Research Backend
        ↓
Attendance / Student / Bus / Notification Data
        ↓
Face Recognition Service
```
Flow đăng ký ảnh học sinh:
```
Parent App
→ Open Camera
→ Capture Student Face
→ Local Face Detection Check
→ Multipart Upload
→ Backend
→ Face Data / Recognition System
```
Flow attendance thực tế:
```
Camera / Recognition Device
→ Identify Student
→ Update Attendance
→ Backend
→ Parent / Teacher / Driver Interfaces
→ Notification
```
## My Contribution
### Core Research & Requirements
Tôi tham gia từ giai đoạn hình thành project và là một trong ba core members ban đầu. Contribution gồm phân tích vấn đề học sinh bị bỏ quên trên xe, tham gia xây dựng solution idea, phân tích requirements, thiết kế application flow, tham gia database design, xác định user roles và các trạng thái cần theo dõi, và thiết kế luồng student onboarding / attendance / notification.
### UI/UX Design
Tôi trực tiếp tham gia thiết kế application bằng **Figma**, xây dựng giao diện và flow cho các role, đặc biệt là Parent experience.
### Flutter Development
Git history cho thấy tôi là primary contributor của phần lớn **Parent module**, gồm Parent Home, Student Information, Parent Settings, Student Notifications, Safe/Emergency/Solve status screens, Student Bio Update, Parent API integration, camera permission và CameraController, capture student face image, local face detection, multipart image upload và integration với backend recognition service.
Tôi cũng tham gia integration/fix code trong quá trình project phát triển.
### AI / Backend Boundary
Tôi **không train hoặc phát triển AI recognition model** và không phải backend owner. Phần của tôi là:
```
Application / Camera / Image Capture
→ Backend Integration
→ Receive Recognition Result
→ Display / Update Student State
```
Backend và AI model do các thành viên khác trong research team phát triển.
## Research & Intellectual Property Result
Công trình có **đơn đăng ký sáng chế đã được công bố**, không ghi nhận là đã được cấp bằng.
**Application No.:** 1-2025-01616  
**Publication No.:** 111439 A  
**Ngày nộp:** 07/03/2025  
**Ngày công bố:** 26/05/2025  
**Tên công trình:** _Thiết bị điểm danh tự động học sinh trên xe buýt sử dụng trí tuệ nhân tạo_  
**Chủ đơn:** Đại học Quốc gia Thành phố Hồ Chí Minh
Tôi được liệt kê trong danh sách tác giả/nhà sáng chế của công trình cùng các thành viên research team.
## Technical Notes & Challenges
Giá trị kỹ thuật chính của project không chỉ nằm ở Flutter UI mà ở việc biến một safety problem thành một end-to-end research system:
```
Real-world Safety Problem
→ Requirements
→ Attendance Logic
→ Face-registration Flow
→ Mobile Application
→ Backend / AI Integration
→ Notification & Tracking
→ Research Prototype
```
Một challenge quan trọng là đảm bảo application flow phản ánh đúng trạng thái thật của học sinh: `chưa lên xe`, `đã lên xe`, `đã xuống xe`, `safe`, `emergency` và trạng thái đã xử lý. Parent application phải nhận dữ liệu từ backend và trình bày trạng thái đủ rõ để phụ huynh hiểu được tình trạng hiện tại.
Face-image enrollment cũng cần xử lý camera permission, image capture, kiểm tra ảnh có khuôn mặt và gửi multipart data tới backend.
## Limitations & Technical Debt
Project đạt mức **functional research demo**, chưa được triển khai rộng rãi trong môi trường trường học thực tế.
Archived mobile source vẫn còn một số đặc điểm của prototype: một số user/parent ID được hard-code trong API integration, một số screen còn sử dụng mock/static data, location/map flow chưa hoàn thiện hoàn toàn, authentication/session handling chưa production-grade, một số API/config được hard-code, automated testing còn rất hạn chế và backend/AI/mobile app chưa được đóng gói thành một production deployment hoàn chỉnh.
## What I Learned
Project giúp tôi có kinh nghiệm khác biệt so với các university coding project thông thường: tham gia từ lúc problem còn ở mức idea, phân tích requirement từ một vấn đề an toàn thực tế, thiết kế application flow và database, thiết kế UI/UX bằng Figma, xây mobile application bằng Flutter, làm việc với camera và image upload, tích hợp mobile app với backend/AI service, làm việc trong research team có nhiều chuyên môn khác nhau và chuyển một research concept thành một demo end-to-end có thể trình bày.
Nếu xây lại theo production standard, tôi sẽ chuẩn hóa session/authentication, configuration management, API abstraction, test coverage, location tracking và device/backend integration; đồng thời thiết kế rõ hơn cơ chế retry/offline/error handling cho attendance events.
## Current Status & References
Project được giữ như một **research/innovation project quan trọng**, thể hiện khả năng của tôi trong requirements analysis, product/application thinking, UI/UX, Flutter development và integration với AI/backend systems.
Đây không phải project mà tôi dùng để claim chuyên môn AI model training; giá trị chính của contribution nằm ở **core research participation + application design + Parent mobile application + face-recognition system integration**.

---

# PROJECT — Farming Assistance

## Overview
**Tên project:** Farming Assistance  
**Thời gian:** 2024-02-25 → 2024-05-28  
**Trạng thái:** Completed / Archived  
**Loại project:** University Team Project — Principles of Database Management (PDM), International University - VNUHCM  
**Vai trò của tôi:** Frontend Lead, UI Designer, Requirements & Database Design Contributor  
**Portfolio priority:** Low–Medium — Academic / Supporting Project
	Farming Assistance là project của môn **Principles of Database Management (PDM)**. Mục tiêu chính của project không chỉ là xây một website hoạt động được mà là áp dụng quy trình phân tích yêu cầu và thiết kế một relational database cho bài toán thực tế, sau đó kết nối database với một full-stack application.
	Trong team, tôi giữ vai trò **Frontend Lead** và là người code frontend chính do các thành viên frontend còn hạn chế kinh nghiệm. Ngoài frontend, tôi tham gia chính vào **phân tích yêu cầu, thiết kế database** và **thiết kế toàn bộ giao diện bằng Figma**.
## Academic Context & Problem
PDM tập trung vào relational database model, ER/EER modeling, chuyển ERD thành relational schema, relational algebra, SQL, keys/functional dependencies và normalization. Vì vậy giá trị học thuật chính của Farming Assistance nằm ở quá trình chuyển một bài toán nghiệp vụ thành mô hình dữ liệu có entity, relationship, primary/foreign key và các ràng buộc phù hợp.
Project mô phỏng một hệ thống hỗ trợ giao dịch giữa **Farmer**, **Supplier** và **Admin**. Farmer quản lý sản phẩm/inventory và theo dõi giao dịch; Supplier xem sản phẩm, tạo order, theo dõi transaction và gửi complaint; Admin theo dõi transaction/complaint và quản lý farming tips.
## Scope & Core Features
Hệ thống có ba role chính:
- **Farmer:** profile, inventory/product management, farming tips và transaction history.
- **Supplier:** profile, product store, cart/order flow, transaction/detail và complaint.
- **Admin:** profile, farming tips, complaints, transactions và order details.
Các chức năng chính gồm login theo role, profile management, inventory CRUD, product browsing, cart/order, transaction tracking, complaint flow, farming tips và avatar upload.
Backend tồn tại trong cùng repository để hoàn thiện application, nhưng backend implementation không phải contribution chính của tôi.
## Tech Stack
**Frontend:** React 18, React Router, Redux Toolkit, React Redux, Axios, Tailwind CSS, DaisyUI, Ant Design, Formik/Yup.  
**Backend của team:** Node.js, Express, Sequelize.  
**Database:** MySQL / relational database.  
**API documentation:** Swagger/OpenAPI setup.  
**File upload:** Multer và local file storage trong archived implementation.  
**Design:** Figma.  
**Version control:** Git/GitHub.
## Architecture & Database
Application có kiến trúc client-server tương đối đơn giản:

```
React Frontend
→ Redux / Service Layer
→ HTTP API
→ Express Routes
→ Controllers
→ Sequelize Models
→ MySQL
```
Frontend được chia theo role và route:
```
Admin
├─ Profile
├─ Tips
├─ Complaints
└─ Transactions

Farmer
├─ Profile
├─ Inventory
├─ Tips
└─ Transactions

Supplier
├─ Profile
├─ Store
├─ Cart
└─ Transactions
```
Database trong final source có các entity chính: `Account`, `Role`, `Admin`, `Farmer`, `Supplier`, `Payment`, `InventoryProduct`, `Order`, `Transaction`, `Complaints` và `FarmingTips`.
Một số relationship quan trọng:
- `Account` gắn với `Role`, sau đó liên kết tới profile `Admin`, `Farmer` hoặc `Supplier`.
- `Farmer` sở hữu nhiều `InventoryProduct`.
- `Order` liên kết `Farmer`, `Supplier`, `InventoryProduct` và `Transaction`.
- `Transaction` thuộc về Supplier và chứa nhiều Order.
- `Complaint` liên kết Supplier, Farmer và sản phẩm liên quan.
- Farmer/Supplier có thông tin payment riêng.
Phần database design là một trong những contribution học thuật chính của tôi: tham gia phân tích requirement, xác định entity/relationship và xây cấu trúc dữ liệu phù hợp với business flow của project.
## API, Authentication & Data Flow
Backend chia API theo role: `/admin`, `/farmer`, `/supplier` và `/auth`. Supplier có các API cho store, order, search, transaction, product detail và complaint; Farmer có profile, inventory, tips và transaction; Admin có tips, complaints, transactions và order detail.
Frontend sử dụng Redux/service layer cho nhiều flow nhưng archived code vẫn có một số API call trực tiếp trong component.
Authentication của archived version chỉ ở mức project học tập. Login kiểm tra `roleID`, username và password trong database; password trong final controller được so sánh trực tiếp và response trả một object chứa `userID`, không phải một JWT được ký thực sự. Repository có dependency liên quan đến JWT/bcrypt nhưng final login flow không sử dụng chúng đầy đủ. Vì vậy đây không phải security model phù hợp cho production.
## My Contribution
### Frontend Lead
Tôi setup/base frontend, tổ chức routing và giữ vai trò code chính ở phía frontend. Git history thể hiện contribution lớn vào:
- Application routing và layout.
- Login/logout và authentication flow phía frontend.
- Redux user state, thunk, service và local persistence.
- Profile flow.
- Supplier role gần như đầy đủ: Store → Cart/Order → Transaction → Transaction Detail → Complaint.
- Một phần Farmer inventory/profile/transaction và các fix liên quan đến API integration.
- Resolve conflict, merge/integrate code và hỗ trợ sửa phần frontend của các thành viên khác.
Vì hai thành viên frontend còn yếu hơn về coding, tôi thường phải review, hỗ trợ fix và hoàn thiện các flow để frontend có thể tích hợp được với backend.
### Requirements & Database Design
Tôi tham gia chính vào việc đọc đề, phân tích requirement và chuyển requirement thành database design. Đây là phần quan trọng vì project thuộc PDM và mục tiêu học tập chính là hiểu cách thiết kế relational database từ specification thay vì chỉ sử dụng database có sẵn.
### UI/UX
Tôi trực tiếp thiết kế **toàn bộ giao diện trên Figma**, sau đó frontend team triển khai dựa trên design đó. Vì vậy project này cũng là một trong những project đầu giúp tôi kết hợp product/UI thinking với database và frontend implementation.
## Technical Notes & Challenges
Thách thức chính của project nằm ở việc đồng bộ ba góc nhìn cùng lúc: **business requirement → relational data model → frontend flow**. Các entity như Order, Transaction, Farmer, Supplier và InventoryProduct phải được thiết kế sao cho frontend có thể hiển thị đúng relationship và backend truy xuất được dữ liệu cần thiết.
Ở frontend, Supplier flow là phần phức tạp nhất tôi phụ trách vì state đi qua nhiều bước: xem sản phẩm → thêm cart → tạo order → tạo/đọc transaction → xem detail → complaint. Git history cũng cho thấy nhiều lần tôi phải sửa API-response mismatch, profile state, transaction detail và integration giữa code của các member.
## Limitations & Lessons
Project được xây cho mục tiêu học tập nên còn nhiều technical debt: authentication chưa an toàn, error handling chưa thống nhất, một số API call bị hard-code `localhost`, automated tests gần như không có và frontend vẫn có logic/API access chưa được abstraction đồng nhất.
Điều tôi học được quan trọng nhất không chỉ là React. Project giúp tôi hiểu rõ hơn quy trình:
```
Requirement
→ Entity / Relationship Analysis
→ Relational Schema
→ Database Implementation
→ Backend API
→ Frontend Business Flow
```
Tôi củng cố kiến thức về ERD, primary/foreign key, relational relationships, normalization mindset, SQL/database design, đồng thời có thêm kinh nghiệm FE leadership, Figma, API integration và hỗ trợ những thành viên có mức coding khác nhau.
Nếu xây lại, tôi sẽ chuẩn hóa authentication, API/error layer, dùng TypeScript, thêm automated tests và document ERD/database decisions rõ hơn.
## Current Status & References
Project đã hoàn thành và không còn được ưu tiên phát triển. Tôi giữ nó như một **academic project quan trọng cho nền tảng database design**, đồng thời là bằng chứng sớm cho khả năng dẫn dắt frontend và chuyển requirement thành cả UI lẫn data model.
**GitHub:** [https://github.com/GSYNDRA/farming-assistance.git](https://github.com/GSYNDRA/farming-assistance.git)

---
# PROJECT — Manach
## Overview
**Tên project:** Manach — Fruit Selling & Warehouse Management System  
**Thời gian:** 2024-04-08 → 2024-05-29  
**Trạng thái:** Completed / Archived  
**Loại project:** University Team Project — Software Engineering, International University - VNUHCM  
**Team size:** 9 members theo project report  
**Vai trò của tôi:** Frontend Lead, Frontend Developer, Integration & Testing Contributor  
**Portfolio priority:** Low–Medium — Academic / Supporting Project
	Manach là project của môn **Software Engineering**. Hệ thống mô phỏng một nền tảng quản lý cửa hàng trái cây, kết hợp customer shopping flow với phần quản trị store, warehouse, inventory và dashboard.
	Trong report chính thức tôi được ghi là **Frontend Developer**, nhưng trên thực tế tôi giữ vai trò gần với **Frontend Lead**: tham gia tổ chức frontend, code nhiều flow chính, hỗ trợ/fix code cho các frontend developer khác và tham gia testing/integration. Tôi **không phải UI/UX designer** của project; phần design do thành viên chuyên trách thực hiện, còn tôi chủ yếu review và chốt lại design trước khi triển khai.
## Academic Context & Problem
Môn Software Engineering tập trung vào toàn bộ software-development lifecycle thay vì chỉ code: project planning, Scrum, requirements, use case/UML, architecture, implementation, testing, delivery và teamwork.
Course guideline yêu cầu team đi qua ba giai đoạn lớn:
```
Requirements & Planning
→ System Design
→ Implementation & Testing
```
Project report của Manach cũng mô tả timeline từ feasibility/requirements, scope, UI wireframe và database schema đến technology selection, frontend/backend development, integration, system testing, deployment preparation và monitoring.
Bài toán của Manach là giảm các vấn đề trong quản lý fruit store/warehouse như nhập liệu thủ công, inventory thiếu chính xác, reporting hạn chế và UI khó sử dụng. Hệ thống hướng tới việc quản lý catalog, order, warehouse/inventory và dòng hàng giữa warehouse với store hiệu quả hơn.
## Scope & Core Features
Frontend được chia thành hai application area chính.
**Customer area:**
- Home và product discovery.
- Fruit store/category pages.
- Cart.
- Order.
- Checkout.
- Profile/settings.
- Login/signup.
**Admin area:**
- Admin home.
- Store/product management.
- Warehouse.
- Inventory.
- Re-order.
- Stock adjustment.
- Order history.
- Dashboard và các chart/statistics.
- Account/settings.
Backend/database thuộc phần việc của backend team; archive `manach-frontend` hiện tại chỉ chứa frontend source.
## Tech Stack
**Frontend:** React 18, Vite, React Router, Redux Toolkit, React Redux.  
**Networking:** Axios; một số archived module sử dụng native `fetch`.  
**UI:** Tailwind CSS, DaisyUI, Ant Design.  
**Forms:** Formik, Yup.  
**Charts:** Chart.js, react-chartjs-2, Recharts.  
**Persistence:** localStorage cho một số user/cart state.  
**Version control:** Git/GitHub.  
**Project methodology:** Software Engineering lifecycle, team collaboration và Scrum-oriented planning theo course guideline.
## Architecture & Application Structure
Frontend được tổ chức theo role/layout:
```
React Application
├─ Auth Area
│  ├─ Welcome
│  ├─ Login
│  └─ Signup
├─ Customer Area
│  ├─ Home
│  ├─ Store
│  ├─ Order
│  ├─ Checkout
│  └─ Settings
└─ Admin Area
   ├─ Home
   ├─ Store
   ├─ Warehouse
   ├─ Dashboard
   └─ Settings
```
State dùng Redux cho user, cart, dashboard, store và loading. Một số API được gom vào service layer như `userService`, `cartService`, `storeService` và `dashboardService`.
Data flow điển hình:
```
Page / Component
→ Redux Thunk or Service
→ REST Backend
→ Redux / Component State
→ UI
```
Project report mô tả system-level architecture/database/backend rộng hơn, nhưng vì repository hiện tại chỉ chứa frontend và contribution của tôi là phía frontend, tôi không sử dụng project này để claim backend/database implementation.
## Data, API & User Flow
Frontend kết nối backend local qua REST API. Các flow nhìn thấy rõ trong source gồm login/signup, user profile, product/store data, checkout/order, dashboard và store management.
Customer flow điển hình:
```
Login
→ Browse Store
→ Add to Cart
→ Checkout
→ Order
→ Profile / Settings
```
Admin flow:
```
Login
→ Admin Home
→ Store / Warehouse
→ Inventory / Re-order / Stock Adjustment
→ Dashboard & Statistics
```
Archived code có local persistence cho user role/user ID và cart. Security/authentication ở project này chỉ nên được xem là demo-level vì frontend dùng local state/storage và không thể hiện một production-grade authorization model trong repository này.
## My Contribution
### Frontend Lead & Core Development
Tôi phụ trách hoặc đóng góp mạnh vào:
- Application routing và việc tách Customer/Admin/Auth areas.
- Authentication pages/flow và user state.
- Customer checkout và các fix liên quan store/order/checkout.
- Admin Home.
- Admin Store và add-product flow.
- Admin Dashboard.
- Nhiều chart/statistic components trong dashboard.
- Admin/User Settings.
- Menu, user information và logout.
- Redux setup cho user, dashboard và store.
- API service/integration ở nhiều flow.
Git history cũng cho thấy tôi thường xuyên merge branch của các frontend member, giải quyết integration issue và sửa các flow khi code từ nhiều người được ghép vào cùng application.
### Team Support & Testing
Do một số thành viên frontend còn yếu về coding, tôi thường hỗ trợ debug/fix và hoàn thiện code để đảm bảo các phần có thể chạy cùng nhau. Tôi cũng tham gia system testing, kiểm tra các flow sau integration và sửa lỗi trước khi hoàn thiện project.
### UI/UX Design
Tôi không trực tiếp thiết kế UI/UX ban đầu. Team có thành viên riêng phụ trách UX/UI. Vai trò của tôi ở phần này là **review/chốt design**, đánh giá khả năng triển khai và sau đó dẫn dắt việc hiện thực hóa design phía frontend.
## Technical Notes & Challenges
Giá trị kỹ thuật lớn nhất của Manach không nằm ở một thuật toán phức tạp mà nằm ở **team-scale integration**. Frontend có nhiều developer làm song song trên customer store, warehouse, inventory, re-order, stock adjustment, dashboard và settings; vì vậy routing, shared state và merge/integration cần được kiểm soát để tránh phá vỡ flow khác.
Dashboard là một trong những phần tôi đóng góp nhiều: dữ liệu từ API được chuyển thành các overview/statistical component như product distribution, orders, warehouse activities, best-selling/revenue và customer indicators.
Một challenge khác là codebase không hoàn toàn thống nhất cách gọi API: có module dùng Axios/service layer trong khi một số phần dùng `fetch` trực tiếp. Điều này làm integration và error handling khó đồng nhất hơn.
## Limitations & Lessons
Archived project vẫn mang tính university project: base URL được hard-code về localhost, chưa có TypeScript, authentication/authorization chưa production-grade, API abstraction chưa đồng nhất và automated tests không đáng kể.
Tuy nhiên đây là project quan trọng về **Software Engineering process**. Tôi có cơ hội thực hành không chỉ coding mà còn:
- Làm việc trong team nhiều role: leader/backend, UX/UI và frontend.
- Nhận requirement và triển khai theo scope.
- Phối hợp frontend-backend.
- Merge/integrate code từ nhiều developer.
- Review và hỗ trợ member yếu hơn.
- System testing và bug fixing.
- Cân bằng giữa design mong muốn và khả năng triển khai thực tế.
Nếu xây lại, tôi sẽ chuẩn hóa API layer, route/role guard, error/loading handling, TypeScript và automated tests; đồng thời áp dụng quy trình code review/branching rõ hơn để giảm integration debt.
## Current Status & References
Project đã hoàn thành và được giữ như một **Software Engineering academic project**, thể hiện kinh nghiệm sớm của tôi trong FE leadership, teamwork, integration và testing trên một application có nhiều module và nhiều developer.
**GitHub:** [https://github.com/nikola0x0/manach-frontend.git](https://github.com/nikola0x0/manach-frontend.git)

---

# PROJECT — BC64 Capstone Movie
## Overview
**Tên đầy đủ:** BC64 Capstone Movie — Movie Theater Website  
**Thời gian:** 2024-03-22 → 2024-04-22  
**Trạng thái:** Completed / Archived  
**Loại project:** Practical Training / Team Project tại Cybersoft  
**Team size:** 2  
**Vai trò của tôi:** Frontend Developer  
**Portfolio priority:** Low — Supporting / Historical Project
Đây là một dự án thực chiến trong quá trình tôi được đào tạo Frontend tại Cybersoft. Nhóm xây dựng một SPA mô phỏng website rạp chiếu phim và sử dụng Cybersoft Movie API làm backend. Flow chính của sản phẩm đi từ xem danh sách phim, xem chi tiết và lịch chiếu, đăng nhập, chọn ghế đến đặt vé.
## Context & Scope
Project tập trung vào kỹ năng xây dựng frontend có dữ liệu thật và business flow nhiều bước. Phạm vi chính gồm movie listing/detail, lịch chiếu theo hệ thống và cụm rạp, authentication UI, user profile, seat selection, ticket booking, responsive UI, API integration và shared state management.
Backend, database, payment gateway và production-grade authentication không nằm trong scope do dữ liệu và nghiệp vụ backend được cung cấp bởi Cybersoft API.
## Core Features
Các chức năng chính gồm:
- Home page, banner/carousel và danh sách phim.
- Movie detail và lịch chiếu.
- Thông tin hệ thống/cụm rạp.
- Login, signup và user profile.
- Protected booking page.
- Sơ đồ ghế với trạng thái ghế thường, VIP, đã đặt và đang chọn.
- Chọn/bỏ chọn ghế, tính tổng tiền và gửi booking request.
- News/app introduction, responsive navigation và global loading UI.
## Tech Stack
**Language:** JavaScript.  
**Frontend:** React 18, React Router DOM, Redux Toolkit, React Redux.  
**Networking:** Axios, Cybersoft Movie REST API.  
**UI:** Tailwind CSS, Ant Design, Font Awesome/React Icons, Lottie React.  
**Forms & validation:** Formik, Yup.  
**Utilities:** Moment.js, react-responsive.  
**Deployment:** Vercel.  
**Backend/Database:** External services provided by Cybersoft; team không trực tiếp xây dựng.
## Architecture
Project là React SPA, source được chia theo `pages`, `components`, `templates`, `HOC`, `redux` và `service`.
Luồng dữ liệu chính:
```
Pages / Components
→ Templates / HOC
→ Redux Toolkit
→ Async Thunks
→ Service Layer
→ Axios
→ Cybersoft REST API
```
API calls được gom vào các service như `movieService`, `ticketService` và `userService` thay vì gọi trực tiếp rải rác trong component. Redux được dùng cho những state cần chia sẻ như movie/screen data, user, seat list, selected seats, booking state và loading.
## Data, API & Authentication
Frontend sử dụng các nhóm API chính cho movie/banner/detail, cinema/schedule, seat list/ticket booking và user authentication/account information.
Authentication dựa trên access token trả về từ Cybersoft API. Sau login, user data/access token được đưa vào Redux và có persistence qua `localStorage`; booking request gửi Bearer token. `CheckUser` HOC được dùng để chặn booking/profile khi chưa đăng nhập.
Đây là cơ chế phù hợp với project đào tạo nhưng không phải production security model: API token nằm phía frontend, authentication state phụ thuộc `localStorage`, authorization guard chủ yếu ở client và không có refresh-token flow do backend không thuộc project.
## My Contribution
Git history và final source cho thấy tôi đóng góp mạnh vào core user flow, đặc biệt:
- Base project và một phần routing.
- Movie carousel, movie detail và movie schedule.
- Booking/screen page, ticket information và ticket booking flow.
- Logic chọn ghế, seat state và booking thunk.
- Movie Redux state, Redux store và loading reducer.
- Phần lớn API configuration, movie service và ticket service.
- Auth template, login flow, local user persistence và global loading UI.
Một số phần được phối hợp giữa hai thành viên như app routing, Header, movie list/detail/schedule, seat UI, authentication state và service integration. Teammate phụ trách nhiều hơn ở signup, profile, multiplex, quick news/filter, footer và một phần lớn navigation.
## Technical Notes & Decisions
**Redux Toolkit cho booking state:** Seat list, selected seats và ticket summary cần được nhiều component dùng chung; đưa state vào Redux giúp `ListChair` và `BuyTicket` dùng cùng một source of truth, đổi lại có thêm Redux boilerplate.
**Service Layer cho REST API:** Tách API calls khỏi component giúp giảm coupling, gom base URL/header và giữ UI tập trung vào rendering/interaction.
**Vấn đề kỹ thuật đáng chú ý:** Booking flow cần đồng bộ seat data từ API → trạng thái đã đặt/đang chọn → tổng tiền → booking payload. Schedule data cũng có cấu trúc lồng Movie → Cinema System → Cinema Cluster → Schedule nên cần transform trước khi render.
Git history ghi nhận một commit `fix bug buyTicket` và một lỗi configuration `MA_NHOM` khiến movie list không trả đúng dữ liệu; group sau đó được điều chỉnh để API hoạt động đúng.
## Limitations, Technical Debt & Lessons
Project không có automated test suite đáng kể; testing chủ yếu là manual UI/API testing cho login, detail, seat selection, booking và responsive layout. Không có performance benchmark, load testing hoặc caching strategy nâng cao.
Các technical debt chính gồm hard-coded API configuration, JavaScript thay vì TypeScript, error handling chưa thống nhất, authentication chưa production-ready, automated testing yếu và một số component/business logic còn khá lớn.
Project giúp tôi thực hành React component development, routing, Redux Toolkit, async API handling, Axios, validation, local persistence và Git collaboration. Điểm quan trọng nhất là chuyển từ các UI độc lập sang một flow có nhiều bước và state liên kết:
```
Browse → Detail → Schedule → Login → Seat Selection → Booking
```
Nếu xây lại, tôi sẽ dùng TypeScript, environment variables, auth interceptor, standardized error handling, tách business logic tốt hơn và viết test cho booking flow.
## Current Status & References
Project không còn được ưu tiên phát triển và được giữ như một learning/practical project trong giai đoạn đào tạo Cybersoft.
**GitHub:** [https://github.com/lhduc141/BC64_Capstone_Movie](https://github.com/lhduc141/BC64_Capstone_Movie)  
**Cybersoft Movie API:** [https://movienew.cybersoft.edu.vn/swagger/index.html](https://movienew.cybersoft.edu.vn/swagger/index.html)  
**Historical deployment:** Vercel deployment từng được ghi trong README.  
**Project management:** Trello.

---

# PROJECT — V-Learning
## Overview
**Tên project:** V-Learning  
**Thời gian:** 2024-04-07 → 2024-05-23  
**Trạng thái:** Completed / Archived  
**Loại project:** Practical Training / Team Project tại Cybersoft  
**Team size:** 2  
**Vai trò của tôi:** Frontend Developer — tập trung chủ yếu vào user-facing course flow  
**Portfolio priority:** Low — Supporting / Historical Project
	Đây là dự án thực chiến trong quá trình đào tạo tại Cybersoft, xây dựng frontend cho một nền tảng e-learning sử dụng Cybersoft E-Learning API. So với BC64 Movie, project có phạm vi application lớn hơn với course enrollment, user information, pagination và một khu vực admin có CRUD cho user/course.
## Context & Scope
Project được chia thành hai nhóm chức năng chính. Phía user cho phép khám phá khóa học, xem detail, đăng ký khóa học và xem thông tin/các khóa học đã đăng ký. Phía administrator có các màn hình quản lý user và course, bao gồm create/update/delete và upload ảnh khóa học.
Backend, database, payment, video-learning infrastructure và production RBAC không nằm trong scope vì project sử dụng API có sẵn từ Cybersoft.
## Core Features
**User-facing:** Home page, course discovery/listing, pagination, course detail, enrollment, enrollment success, user profile, registered courses, blog/content pages, login và signup.
**Admin:** Admin layout/dashboard structure, user list/CRUD, course list/CRUD, course image upload, search/filter và MUI DataGrid tables.
## Tech Stack
**Language:** JavaScript.  
**Frontend:** React 18, React Router, Redux Toolkit, React Redux.  
**Networking:** Axios, Cybersoft E-Learning REST API.  
**UI:** Tailwind CSS, DaisyUI, Material UI, MUI DataGrid, Ant Design, Font Awesome, Swiper.  
**Forms & validation:** Formik, Yup.  
**Feedback:** react-hot-toast, SweetAlert2.  
**Persistence:** localStorage.  
**Backend/Database:** External Cybersoft API.
## Architecture
Application được tách thành các khu vực routing/layout riêng:
```
React Routes
├─ HomeTemplate
│  ├─ Home
│  ├─ Courses
│  ├─ Course Detail
│  ├─ User Profile
│  └─ Blog
├─ AuthTemplate
│  ├─ Login
│  └─ Signup
└─ AdminTemplate
   ├─ Users
   └─ Courses
```
Luồng data chính:
```
Pages / Components
→ Redux Toolkit / Async Thunks
→ Services
→ Axios
→ Cybersoft E-Learning API
```
Redux quản lý các state chính liên quan đến course list/detail/enrollment và user. Admin sử dụng MUI DataGrid để giảm thời gian tự xây table behavior.
## Data, API & Authentication
Các course APIs được dùng cho list, pagination, category, detail, enrollment, create/update/delete course và image upload. User APIs gồm login/signup, account information, user detail/type/list và CRUD user.
Login nhận access token, lưu authentication state vào Redux/localStorage và dùng token cho Authorization header. Khi reload, application gọi account API để phục hồi user state. Admin area có client-side guard trong `AdminTemplate`.
Archived implementation chưa phải production authorization: admin được xác định bằng account/email hard-coded phía frontend, token được lưu localStorage và project không có proper RBAC/refresh-token strategy.
## My Contribution
Git history cho thấy tôi tập trung mạnh vào **user-facing course flow** và phần state/API tương ứng:
- Course listing/show components, detail và course introduction.
- Course enrollment, enrollment success và paginated course page.
- User information và registered-course display.
- Course Redux slice, async thunks, course service và course local persistence.
- Phần lớn user async thunk và một phần authentication/user state.
- Footer, blog, feedback, event/more-information sections, một phần Home Page và Header.
- Initial repository/base source, library setup, initial templates và `AuthTemplate`.
Teammate phụ trách nhiều hơn ở admin user/course management, DataGrid/admin sidebar/template, create/update user/course, phần lớn login/signup UI, carousel/HomeIntro và một phần lớn Header.
## Technical Notes & Decisions
- **Redux Toolkit cho course flow:** Course list/detail/enrollment được tổ chức theo async thunk → service → API → Redux state → render, giúp tách network request khỏi component.
- **Tách Home/Auth/Admin template:** Việc phân vùng routing/layout giúp trách nhiệm của public area, authentication area và administration area rõ ràng hơn.
- **MUI DataGrid cho admin:** Giúp triển khai CRUD table nhanh với behavior sẵn có, nhưng tạo dependency tương đối lớn cho scope project.
- **Vấn đề đáng chú ý:** Authentication state cần đồng bộ login API → Redux → localStorage → token → reload → restore account. Archived source cho thấy login từng gặp lỗi và có workaround với sự hỗ trợ của mentor. Một số inconsistency vẫn còn ở bản cuối, như component gọi `setInfoUser` không đồng nhất với slice và naming/local persistence chưa hoàn toàn nhất quán.
## Limitations, Technical Debt & Lessons
- Project gần như không có automated tests; testing chủ yếu là manual UI/API testing cho authentication, enrollment, admin CRUD, routing và validation.
- Technical debt chính gồm authentication logic chưa sạch, hard-coded admin identity, token/localStorage handling chưa production-ready, error handling rải rác, không có TypeScript, naming typo và API cache/state chưa được quản lý theo production standard. Archived UI cũng có chỗ render dữ liệu nhạy cảm không phù hợp, vì vậy cách này không nên được reuse.
- Project giúp tôi hiểu rõ hơn cách tổ chức một React application thành Public/User Area, Authentication Area và Admin Area; đồng thời thực hành CRUD, pagination, enrollment flow, shared state, API integration và phân chia feature giữa hai frontend developers.
- Nếu xây lại, tôi sẽ dùng TypeScript, proper role-based authorization, environment configuration, Axios/auth interceptor, standardized loading/error state, query caching như RTK Query và test cho auth/course/admin CRUD.
## Current Status & References
Project không còn được ưu tiên phát triển và được giữ như một minh chứng cho giai đoạn đào tạo Cybersoft, khi tôi chuyển từ React UI/component development sang application có API, authentication, user flow, admin CRUD và shared application state.
**GitHub:** [https://github.com/lhduc141/vlearning](https://github.com/lhduc141/vlearning)  
**Cybersoft E-Learning API:** [https://elearningnew.cybersoft.edu.vn/swagger/index.html](https://elearningnew.cybersoft.edu.vn/swagger/index.html)  
**Project management:** Trello.

---

# PROJECT — NeoPac Ninja
## Overview
**Tên project:** NeoPac Ninja  
**Thời gian:** 2023-09-28 → 2024-01-12  
**Trạng thái:** Completed / Archived  
**Loại project:** Team / Learning Game Project  
**Team size:** 5 contributors xuất hiện trong Git history  
**Vai trò của tôi:** JavaScript Game Developer / Core Gameplay Contributor  
**Portfolio priority:** Low — Supporting / Historical Project
NeoPac Ninja là browser game dạng maze/Pac-Man-style. Người chơi điều khiển một Ninja trong mê cung, tránh enemy, thu thập ba keys và các item hỗ trợ, mở exit rồi hoàn thành game trong thời gian ngắn nhất.
## Context & Scope
Project tập trung vào JavaScript game fundamentals thay vì xây một sản phẩm có backend. Scope gồm HTML Canvas rendering, tile-based map, movement/collision, enemy AI và pathfinding, collectible items, teleport, hidden room, timer, pause/game states và local leaderboard.
Không có backend, online account, cloud leaderboard, multiplayer hay game engine phức tạp.
## Core Features
- Start menu, tutorial và Canvas game screen.
- Ninja movement và sprite animation.
- Wall/enemy/item/teleport/exit collision.
- Enemy patrol và chase behavior.
- BFS-based pathfinding khi Ninja nằm trong detection range.
- Collectible points, ba keys, speed boost, teleport và hidden room.
- Exit unlock, timer, pause/continue, game-over/completed state.
- Music và local leaderboard.
## Tech Stack
**Language:** JavaScript.  
**Frontend/Game:** HTML, CSS, Vanilla JavaScript, HTML Canvas API.  
**Persistence:** Browser `localStorage`.  
**Assets:** Sprite images, audio, Font Awesome, Google Fonts.  
**Backend/API/Database:** Không có.
## Architecture
Game dùng cấu trúc đơn giản, logic chính nằm trong một số file JavaScript:
```
index.html
├─ game.js
│  ├─ game loop / map / game state
│  ├─ rendering / timer
│  └─ leaderboard
├─ ninja.js
│  ├─ movement / collision
│  ├─ item interaction / teleport
│  └─ rendering
├─ enemy.js
│  ├─ patrol / chase / detection
│  ├─ BFS pathfinding
│  └─ collision/rendering
└─ player.js
   └─ leaderboard model
```
Map được biểu diễn bằng 2D matrix; các numeric tile đại diện cho wall, ground, collectible, speed item, teleport, key, exit và hidden area.
## Data, Game Logic & Persistence
Không có server/API. Game chạy hoàn toàn trên browser.
Leaderboard lưu trong `localStorage`, gồm player name và completion time/score rồi được sort theo thời gian hoàn thành.
Enemy có hai trạng thái chính: khi không detect được Ninja thì patrol theo các điểm định trước; khi Ninja nằm trong detection range thì sử dụng BFS trên grid để tìm bước di chuyển tiếp theo. Hidden room làm enemy không detect Ninja.
Game loop chạy khoảng 30 FPS trong archived implementation; với grid nhỏ, BFS đủ cho scope hiện tại nhưng sẽ không scale tốt nếu map hoặc số enemy tăng lớn.
## My Contribution
Git history cho thấy đây là team project, nhưng trong final source phần lớn core gameplay code được ghi nhận dưới authorship của tôi.
Tôi đóng góp mạnh vào:
- `game.js`: main game loop, state, timer, game-over/pass, map handling, item integration, enemy creation, leaderboard và rendering coordination.
- `enemy.js`: behavior, movement, detection range, pathfinding và collision.
- Phần lớn `ninja.js`: character logic, movement, item interaction, teleport, collision và rendering.
- `player.js`: leaderboard model.
- Phần lớn `index.html` và `main.css`.
Các thành viên khác cũng từng đóng góp character movement/animation, enemy movement, pause, hidden rooms, assets và game-state fixes, nên project vẫn được ghi nhận là team project.
## Technical Notes & Decisions
**Tile-based map:** 2D array giúp collision và pathfinding dễ triển khai/quan sát, phù hợp learning project; trade-off là nhiều vị trí bị hard-code và khó mở rộng thành nhiều map lớn.
**HTML Canvas:** Cho phép trực tiếp thực hành rendering loop, sprite và coordinate system mà không phụ thuộc framework/game engine.
**BFS pathfinding:** Phù hợp với grid nhỏ, dễ hiểu và đảm bảo tìm đường theo số bước; nếu game lớn hơn có thể cần A* hoặc path caching.
**localStorage leaderboard:** Không cần backend và đủ cho demo, nhưng dữ liệu chỉ tồn tại trên browser hiện tại.
Các phần khó nhất là đồng bộ grid coordinate với character coordinate cho pathfinding/collision, quản lý nhiều game states, và kết hợp timer với local leaderboard.
## Limitations, Technical Debt & Lessons
Archived code còn nhiều global variables; `game.js` chứa nhiều trách nhiệm, map/item positions hard-coded, rendering và game logic coupling chặt, interval lifecycle chưa được abstraction tốt, không có module/build system và không có automated tests. Game loop cũng chưa dùng `requestAnimationFrame` + delta time.
Project giúp tôi thực hành JavaScript object/class, browser event APIs, Canvas rendering, sprite animation, collision, input handling, game-state management, grid traversal/BFS và Git collaboration.
Git workflow của team gồm personal branch → commit → pull main → resolve conflict → push → pull request → review → merge.
Nếu xây lại, tôi sẽ tách `game.js` thành modules, dùng explicit Game State Machine, tách renderer khỏi game logic, dùng `requestAnimationFrame` + delta time, đưa map ra config riêng và viết tests cho collision/pathfinding.
## Current Status & References
Project không còn được ưu tiên phát triển và được giữ như một learning artifact cho JavaScript, algorithms, Canvas/game loop và Git teamwork.
**GitHub:** [https://github.com/lhduc141/NeoPacNinja](https://github.com/lhduc141/NeoPacNinja)

---

# PROJECT — TCR Netcentric
## Overview
**Tên đầy đủ:** TCR Netcentric — Tower Clash Royale  
**Thời gian:** 2025-04-23 → 2025-06-02  
**Trạng thái:** Completed / Archived  
**Loại project:** University / Team Project — Net-Centric Programming  
**Team size:** 2 contributors trong Git history  
**Vai trò của tôi:** Go Developer / TCP Server & Game Logic Developer  
**Portfolio priority:** Low — Supporting / Historical Project
	TCR Netcentric là một game network đơn giản cho hai người chơi, lấy ý tưởng từ tower battle. Mục tiêu chính của project là thực hành Go và các khái niệm net-centric: raw TCP connection, client/server communication, protocol dạng command, server-side game state, authentication và file-based persistence.
	Git history của final version cho thấy toàn bộ Go source được authored bởi tôi; teammate chủ yếu đóng góp README/technical documentation.
## Context & Scope
Game có TCP server và CLI client. Hai client đăng nhập, server bắt đầu game khi đủ hai authenticated players. Mỗi player có username, EXP, level, mana, troop state và ba tower: Guard Tower 1, Guard Tower 2 và King Tower.
Gameplay theo turn. Player dùng command để summon troop vào lane/target ở attack hoặc defend mode. Mana bắt đầu ở 5, tăng theo round và có giới hạn 10. Guard Tower 1 phải bị phá trước Guard Tower 2; cả hai guard towers phải bị phá trước khi attack King Tower. Phá King Tower là điều kiện thắng.
Scope không bao gồm real-time continuous gameplay, GUI, matchmaking, multiple game rooms, production database, TLS hoặc production authentication.
## Core Features
- Raw TCP server/client trên port `9000`.
- Username/password authentication.
- Two-player game session và turn handling.
- Mana system và troop summon.
- Attack/defend mode, three lanes.
- Guard Tower/King Tower progression.
- Troop-vs-troop và troop-vs-tower combat.
- Tower counterattack, DEF và critical hit.
- Healing troop special ability.
- EXP, level calculation và level-based stat scaling.
- JSON-based player/troop/tower data.
- Server broadcast messages.
Client command chính có dạng:

```
summon <TroopName> <guard|king> <Number> <attack|defend>
end
```
## Tech Stack
**Language:** Go.  
**Go version:** 1.24 trong `go.mod`.  
**Networking:** `net`, raw TCP sockets.  
**I/O:** `bufio`, `io`.  
**Persistence:** JSON, `encoding/json`, `os`.  
**Concurrency primitives:** `sync.Mutex`; client có goroutine để listen server message bất đồng bộ.  
**Database:** Không dùng database server.
## Architecture
```
main.go
→ server package
   ├─ player/session state
   ├─ command processing
   ├─ turn/game loop
   ├─ combat resolution
   └─ broadcast
   ├─ models/
   │  ├─ Troop
   │  └─ Tower
   └─ utils/
      ├─ authentication
      ├─ EXP/level helpers
      ├─ battle helpers
      ├─ JSON loaders
      └─ network helpers

CLI Client
→ TCP
→ Server :9000
→ JSON data files
```
Server hiện tại chỉ quản lý một game session gồm hai người chơi.
## Data, Protocol & Authentication
Project không dùng REST. Client/server trao đổi bằng plain-text TCP commands và text responses cho authentication result, turn prompt, mana, summon/combat/tower result và win/loss.
Dữ liệu lưu trong JSON:
- `players.json`: username, password, EXP.
- `troop_specs.json`: name, HP, ATK, DEF, mana, EXP và special ability.
- `tower_specs.json`: name, HP, ATK, DEF, CRIT và EXP value.
Authentication đọc username/password từ JSON. Khi hợp lệ, server tạo Player object và chờ player thứ hai.
Đây là academic networking implementation, không phải production security: password lưu plain text, không hashing/TLS/token session/brute-force protection và không có secure persistent database.
## My Contribution
Trong final repository, tôi trực tiếp viết toàn bộ Go source, bao gồm:
- TCP server và connection handling.
- Authentication flow và player/session state.
- Turn handling, command parser và summon validation.
- Mana, troop state, tower state, combat, win condition và broadcast.
- Level/EXP scaling.
- CLI client, TCP connection, user input và async server-message listener.
- `Troop`/`Tower` models.
- JSON loading, authentication, EXP/level, healing và network helpers.
- Player-data updates và troop/tower specifications.
Teammate chủ yếu đóng góp README và technical documentation.
## Technical Notes & Decisions
**TCP thay vì HTTP:** Đây là lựa chọn phù hợp với mục tiêu môn Net-Centric Programming vì buộc project làm việc trực tiếp với connection-oriented socket và tự định nghĩa protocol. Trade-off là command parsing/error handling khó hơn REST và client/server coupling cao hơn.
**JSON thay vì database:** Scope nhỏ và trọng tâm nằm ở networking/game logic nên JSON đủ cho player/spec data. Cách này không phù hợp nếu cần concurrent persistence hoặc multi-server.
**Turn-based thay vì real-time:** Giảm đáng kể complexity về synchronization, timing và event ordering, phù hợp với academic scope.
Combat flow ở mức khái quát:
```
Player commands
→ resolve each lane
→ troop vs troop
→ survivor vs tower
→ tower counterattack
→ update HP/DEF
→ check tower destruction
→ check King Tower
```
Tower/troop stats có level scaling theo công thức dạng `base stat × (1 + level × 10%)`.
## Limitations, Known Issues & Lessons
Archived source có một số issue đáng chú ý:
- `GetExp()` đọc `player_data.json` trong khi authentication/update EXP dùng `data/players.json`, có thể làm initial EXP không được load nhất quán.
- Unknown troop có trường hợp trả zero-value troop mà không báo error đủ rõ.
- Khi King Tower bị phá, server gọi `os.Exit(0)`, kết thúc toàn bộ process thay vì chỉ đóng game session.
Technical debt gồm global game state, chỉ một game/session, JSON persistence, plain-text password, không reconnect/disconnect recovery, không matchmaking, không automated tests, command protocol chưa formalized và concurrency model còn đơn giản.
Project giúp tôi thực hành Go package/struct, file I/O, JSON serialization, standard library, TCP client/server, socket lifecycle, server-authoritative state, command validation, shared state, ordering và synchronization.
Nếu xây lại, tôi sẽ tạo `GameSession` riêng, hỗ trợ nhiều rooms, dùng goroutine/channel theo session, formalize protocol bằng JSON messages, tách persistence layer, xử lý reconnect/disconnect, hash password/TLS khi cần và thêm unit/integration tests.
## Current Status & References
Project không còn được ưu tiên phát triển và được giữ như một learning artifact cho Go, TCP networking, client/server architecture, server-side game state và protocol design.
**GitHub:** [https://github.com/lhduc141/tcr_netcentric](https://github.com/lhduc141/tcr_netcentric)
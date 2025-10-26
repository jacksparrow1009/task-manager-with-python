import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

export const authApi = createApi({
  reducerPath: "authApi",
  baseQuery: fetchBaseQuery({
    baseUrl: "http://localhost:8000/auth/",
  }),
  endpoints: (builder) => ({
    registerUser: builder.mutation({
      query: (userData) => ({
        url: "register/",
        method: "POST",
        body: userData,
      }),
    }),
    loginUser: builder.mutation({
      query: (credentials) => ({
        url: "login/",
        method: "POST",
        body: credentials,
      }),
    }),
  }),
});

export const { useRegisterUserMutation, useLoginUserMutation } = authApi;
